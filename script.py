import imaplib
import email
from email.header import Header, decode_header, make_header

# Connection settings
HOST = 'IMAP-SERVER'
USERNAME = 'USERNAME'
PASSWORD = "PASSWORD"

# Connects with the above credentials using IMAP port 993
m = imaplib.IMAP4_SSL(HOST, 993)
m.login(USERNAME, PASSWORD)
m.select('INBOX')

result, data = m.uid('search', None, "ALL")
if result == 'OK':
    for num in data[0].split():
        result, data = m.uid('fetch', num, '(RFC822)')
        if result == 'OK':
            # Gets raw message
            email_message_raw = email.message_from_bytes(data[0][1])   
            # Decode headers (where From: is stored)
            # This can be used to retrieve other fields in email header, for example Reply-to
            email_from = str(make_header(decode_header(email_message_raw['From'])))
            # Print each name and email
            # This will print a list of ['Name', 'Email'], can also just print ['Email'] in case there is no name
            email_addr = email_from.replace('<', '>').split('>')
            # Write email list to .txt
            # We now need to open a pre-created text called emails.txt
            # If length of email_addr is larger than 1, so there's a name and email present, it should get email_addr[1] which is the email field.
            # However, if there's no email, then the list would be just ['Email'], so we need to get index [0].
            with open('emails.txt', 'a') as emailText:
                if len(email_addr) > 1:
                    emailText.write("{}\n".format(email_addr[1]))
                else:
                    emailText.write("{}\n".format(email_addr[0]))
            # Remove duplicates
            # The above code will write each email 'From:' field in the text file, multiple times if you had a conversation back and forth with them.
            # With the following code, after the 'with' block has been closed above, we open the file and read ONLY the unique lines with .readlines().
            # We use set() to convert the text to a unique set, therefore removing duplicate strings
            # We then CREATE a new text file called emailsUnique.txt and write all the unique emails to it.
            unique_emails = set(open('emails.txt').readlines())
            w_unique_emails = open('emailsUnique.txt', 'w').writelines(unique_emails)
            
# We then close the connection and logout from the server to end the cycle.
m.close()
m.logout()
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
            # This can be used to retrieve other fields in email header, for example ['Reply-to']
            email_from = str(make_header(decode_header(email_message_raw['From'])))
            # email_addr will print ['Name', 'Email'], it might also print ['Email'] when there is no 'Name'
            email_addr = email_from.replace('<', '>').split('>')
            # We create a file emails.txt and add conditions for both scenarios, if there is a Name field and when there isn't
            # If length of email_addr is larger than 1 - so there is both Name and Email present, it should get email_addr[1] - the email field.
            # However, if there's no name, then the list would be just ['Email'], so we need to get index [0].
            with open('emails.txt', 'a') as emailText:
                if len(email_addr) > 1:
                    emailText.write("{}\n".format(email_addr[1]))
                else:
                    emailText.write("{}\n".format(email_addr[0]))
            # We open the file and read ONLY the unique lines with .readlines().
            # We use set() to convert the text to a unique set, therefore removing duplicate strings
            # We then create a new text file called emailsUnique.txt and write all the unique emails to it.
            unique_emails = set(open('emails.txt').readlines())
            w_unique_emails = open('emailsUnique.txt', 'w').writelines(unique_emails)
            
# We then close the connection and logout from the server to end the cycle.
m.close()
m.logout()
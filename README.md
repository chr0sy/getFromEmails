# Python script which retrieves and saves to a .txt file all the email addresses in the "From:" field from each email received in a mailbox. 

This is a Python script that:

- Connects to an IMAP server
- Selects and retrieves all the emails in the ‘INBOX’ folder
- Gets raw messages and decodes header from each
- Checks for duplicates and writes the 'From' emails in a .txt file.
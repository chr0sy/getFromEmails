# Python script which retrieves and saves to a .txt file all the email addresses in the "From:" field from each email received in a mailbox. 

There are times where one could want to retrieve all email addresses that a mailbox has received emails from. One of my apps uses a support email which users can use to write us regarding issues they might encounter.

During our launch, we wrote a privacy policy where we informed users who write to us for support purposes and accept our Terms of Services, could be contacted later regarding promotional offers or changes in the app — however, other priority tasks made this small but important detail left behind and never fully developed. The app has continuously grown and so has the support emails, counting ~1000+ as of now.

This is a Python script that:

- Connects to an IMAP server
- Selects and retrieves all the emails in the ‘INBOX’ folder
- Gets raw message and decodes header (where the From: field is stored)
- Checks for duplicates and writes the emails in a .txt file.
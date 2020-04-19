# Send emails with Gmail's API

This program is useful to those who needs to send out HTML emails leveraging Gmails API with or without attachment using Python 3.

## Pre-requisites

Enable the Gmail API and Download **credentials.json** from [Gmail's Developer page](https://developers.google.com/gmail/api/quickstart/python).

Place the **credentials.json** file into your project folder.

You need to install below pip packages to run this program. Use **sudo -H** while installing these packages if you face permission errors.

```bash
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib apiclient oauth2client
```

## Usage


```python3
#It will ask for Google Account Authentication. Allow it to download the token credentials
quickstart.py

#Modify your email's recipient, subject and body details in main.py before running this command
main.py
```

Currently I have made the program to read details from a JSON file. Modify it in main.py as per your wish.

## Credits
[Google (Gmail)](https://mail.google.com) and [HowToFAQ](https://youtu.be/YVgj9ngUlaY)

# EmailSpam
*EmailSpam* is a tool with the purpose of sending large quantities of emails in specified periods of time. 
Depending on the number of emails inputted and delay settings, *EmailSpam* is capable of sending thousands of emails in minutes.

**Please use with caution. *EmailSpam* is not intended for malicious intents.**

## Tutorial
**Choosing target email**: Place the destination email in the [destination file](EmailSpam/Resources/Destination.txt)

**Inputting email accounts to send from**: Place email name(s) (example@gmail.com) - on separate lines, if multiple - in the [MyEmails.txt](EmailSpam/Resources/MyEmails.txt). Each email must have the same password in order to login to multiple emails.

**Message**: This is the message that the email will display

**Emails Per Account**: This is the number of emails sent from each account. For example, if there are 5 accounts, and "Emails Per Account" is set to 10, a total of 50 emails will be sent.

**Delay**: Delay (in seconds) between each email.

## Important Configuration
Please make sure that for **each** of the email accounts inputted, the [less secure apps setting](https://myaccount.google.com/lesssecureapps) is allowed.


## Demo Video
![Alt Text](https://github.com/AlanChen4/EmailSpam/blob/master/EmailSpam/Resources/demo.gif)

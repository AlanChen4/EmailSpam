class emailLoader():

    def load_my_emails(self):
        with open('Resources/MyEmails.txt') as my_emails:
            email_list = my_emails.readlines()
            email_list = [email.strip() for email in email_list]
            print("[{0} Emails Successfully Loaded]".format(len(email_list)))
            return email_list

    def load_destination_email(self):
        with open ('Resources/Destination.txt') as destination:
            destination = destination.readlines()
            if len(destination) > 1:
                print("Error: More than one destination email set")
                return False
            destination = destination[0].strip()
            print("[Destination Email]: {0}".format(destination))
            return destination


from EmailLoader import EmailLoader
from EmailSpammer import EmailSpammer

class Main():

  def __init__(self):
    loader = EmailLoader()
    spammer = EmailSpammer()

    my_emails = loader.load_my_emails()
    destination_email = loader.load_destination_email()
    if destination_email != False:
      spammer.configure_settings(my_emails, destination_email)
      spammer.start_sending()

main = Main()

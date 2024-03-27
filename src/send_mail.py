from mailersend import emails

def send_mail(summary):
    mailer = emails.NewEmail(
        "mlsn.c3bdff3fddfb65c58423c8b3a67af1c54505c3245f65725270f2ba0551acf301"
    )

    # define an empty dict to populate with mail values
    mail_body = {}

    mail_from = {
        "name": "veloxforce",
        "email": "marius@connectveloxforce.info",
    }

    recipients = [
        {
            "name": "Ulrich Wilsch",
            "email": "wilsch@wilsch.de",
        }
    ]

    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(recipients, mail_body)
    mailer.set_subject("Report Aircall", mail_body)
    mailer.set_html_content("", mail_body)
    mailer.set_plaintext_content(summary, mail_body)

    # using print() will also return status code and data
    print(mailer.send(mail_body))

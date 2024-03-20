from mailersend import emails

def send_mail(summary):
    mailer = emails.NewEmail('mlsn.e058e942ede4d87f506a9854c37798e368b3827b238aa7bb87c627ec01b5ee8f')

    # define an empty dict to populate with mail values
    mail_body = {}

    mail_from = {
        "name": "veloxforce",
        "email": "dtunderman@veloxforce.com",
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

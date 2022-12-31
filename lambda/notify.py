import json
from botocore.exceptions import ClientError
import Email as Mailer


def send_email(recipient, subject, body):
    mailer = Mailer(recipient, subject, body)

    try:
        print("Sending email to {}...".format(mailer.recipient))
        print("Subject: {}".format(mailer.subject))
        print("Body HTML: {}".format(mailer.body_html))
        print("Body Text: {}".format(mailer.body_text))
        response = mailer.send()

    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    recipient, subject, body = event['recipient'], event['subject'], event['body']
    send_email(recipient, subject, body)

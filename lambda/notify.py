import json
import boto3
from botocore.exceptions import ClientError
import Email as Mailer

AWS_REGION = "us-west-2"

client = boto3.client('ses', region_name=AWS_REGION)


def send_email(recipient, subject, body):
    mailer = Mailer(recipient, subject, body)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    mailer.recipient,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': mailer._charset,
                        'Data': mailer.body_html,
                    },
                    'Text': {
                        'Charset': mailer._charset,
                        'Data': mailer.body_text,
                    },
                },
                'Subject': {
                    'Charset': mailer._charset,
                    'Data': mailer.subject,
                },
            },
            Source=mailer._sender,
        )

    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    recipient = event['recipient']
    send_email(recipient)

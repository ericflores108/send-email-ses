import boto3


class Mailer:
    def __init__(self, recipient, subject, body):
        """Initialize an Email instance.

        Arguments:
        recipient -- the email address of the recipient
        subject -- the subject of the email
        body -- the body of the email, as a string or list of strings
        """
        if not isinstance(recipient, str) or not recipient.strip():
            raise ValueError("'recipient' must be a non-empty string")
        if not isinstance(subject, str) or not subject.strip():
            raise ValueError("'subject' must be a non-empty string")
        if not isinstance(body, (str, list)) or not body:
            raise ValueError(
                "'body' must be a non-empty string or list of strings")

        self.recipient = recipient
        self.subject = subject
        self.body = body
        self._sender = "Eric Flores <ericflores108@outlook.com>"

    @property
    def body_html(self):
        """Return the HTML version of the email body."""
        body_html = ""
        if isinstance(self.body, str):
            body_html = f"<p>{self.body}</p>"
        else:
            body_html = "<br>".join([f"<p>{line}</p>" for line in self.body])
        return f"""<html><head></head><body>{body_html}<p>Eric Flores</p></body></html>"""

    @property
    def body_text(self):
        """Return the plain text version of the email body."""
        if isinstance(self.body, str):
            return self.body
        else:
            return "\r\n".join(self.body)

    def send(self):
        """Send the email using Amazon SES."""
        client = boto3.client('ses', region_name='us-west-2')
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    self.recipient,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': 'UTF-8',
                        'Data': self.body_html,
                    },
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': self.body_text,
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': self.subject,
                },
            },
            Source=self._sender,
        )
        return response

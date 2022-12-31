class Email:
    def __init__(self, recipient, subject, body):
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self._sender = "Eric Flores <ericflores108@outlook.com>"
        self._aws_region = "us-west-2"
        self._charset = "UTF-8"
        self._sender = "Eric Flores <ericflores108@outlook.com>"

    @property
    def body_html(self, body):
        return f"""<html>
        <head></head>
        <body>
          <p>{body}\r\n</p>
          <p>Eric Flores</p>
        </body>
        </html>
                    """

    @property
    def body_text(self, body):
        return f"{body}\r\n"

#!/usr/bin/env python3
import os

import aws_cdk as cdk

from send_email_cdk.send_email_cdk_stack import SendEmailCdkStack


app = cdk.App()
SendEmailCdkStack(app, "SendEmailCdkStack")

app.synth()

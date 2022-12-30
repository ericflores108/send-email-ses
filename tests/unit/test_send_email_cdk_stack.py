import aws_cdk as core
import aws_cdk.assertions as assertions

from send_email_cdk.send_email_cdk_stack import SendEmailCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in send_email_cdk/send_email_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SendEmailCdkStack(app, "send-email-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

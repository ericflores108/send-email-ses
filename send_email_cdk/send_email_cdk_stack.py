from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    CfnOutput as output,
)


class SendEmailCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        notify = _lambda.Function(
            self, 'NotifyHandler',
            function_name='notify-email-ses',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='notify.handler',
        )

        # add policies to notify
        notify.add_to_role_policy(
            statement=iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "ses:SendEmail",
                    "ses:SendRawEmail",
                    "ses:SendTemplatedEmail"
                ],
                resources=[
                    f"arn:aws:ses:{self.region}:{self.account}:identity/ericflores108@outlook.com",
                    f"arn:aws:ses:{self.region}:{self.account}:identity/flores.eric88@gmail.com"]
            )
        )

        output(self, 'arn', value=notify.function_arn)

from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    CfnOutput
)


class HelloWorldCdkAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Defines an AWS Lambda resource
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset('lambda'), # Directory where code is taken from
            handler='hello.handler', # Filename.method (hello.py for lambda code and handler is the method that will execute first as entry point)
        )

        CfnOutput(self, "LambdaARN", value= my_lambda.function_arn)
        CfnOutput(self, "FunctionName", value= my_lambda.function_name)
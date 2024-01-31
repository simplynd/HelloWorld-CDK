#!/usr/bin/env python3

import aws_cdk as cdk

from hello_world_cdk_app.hello_world_cdk_app_stack import HelloWorldCdkAppStack


app = cdk.App()
HelloWorldCdkAppStack(app, "HelloWorldCdkAppStack")

# app.synth()

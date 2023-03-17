#!/bin/bash

# $chmod +x deploy.sh
# $./deploy.sh staging

# Variables
export AWS_REGION=eu-west-1
export ENVIRONMENT="staging"
export STACK_NAME="testing-function"


sam build
sam deploy \
--profile=latana-${ENVIRONMENT} \
--stack-name "${STACK_NAME}" \
--region "${AWS_REGION}" \
--resolve-s3 \
--parameter-overrides Environment=${ENVIRONMENT} \
--capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND

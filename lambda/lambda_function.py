import os
import boto3
import time
from datetime import date
from aws_lambda_powertools import Logger

timestamp = time.time()

logger = Logger()

QUEUE_URL = os.getenv('QUEUE_URL')

@logger.inject_lambda_context
def lambda_handler(event, context):
    logger.info({"action":"invoke_lambda", "payload":{"event":event}})
    message = {"module":"next_module", "timestamp": timestamp}
    if event.get("send_queue"):
        send_message_queue(message)
    else:
        logger.info({"action":"NO CREATE Q"})
    return "OK"

def send_message_queue(message):
    sqs_client =boto3.client("sqs")
    response = sqs_client.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=str(message),
        DelaySeconds= 120
    )
    logger.info({"action":"send_message_queue", "payload":{"response":response}})

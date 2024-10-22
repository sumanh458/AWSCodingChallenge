import json

import boto3
client = boto3.client('glue')

def lambda_handler(event, context):
    response = client.start_crawler(Name ="schema_inference_crawler")
    print(json.dumps(response,indent=4))

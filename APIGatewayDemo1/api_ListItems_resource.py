import json
import os

def lambda_handler(event, context):
  print (event)
  statusCode = 200
  return {
    "statusCode": statusCode,
    # Imagine this is being loaded from a database
    "body": json.dumps(["EC2", "Lambda", "S3", "RDS"]),
    "headers": {
      "Content-Type": "application/json"
    }
  }

import json
from datetime import datetime

def hello(event, context):
    body = {
        "message": "Hello world",
        "author": "Bakhtiyar Garashov",
        "invoked_at": str(datetime.now())
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

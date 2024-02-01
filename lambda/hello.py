import json

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    print('context: {}'.context)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello From Lambda'
    }
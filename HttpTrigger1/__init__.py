import logging
import requests
import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:

    # get event data from acr
    logging.info('Python HTTP trigger function processed a request.')
    try:
        data = req.get_json()
        event_id = data['id']
        event_time = data['timestamp']
        event_action = data['action']
        event_target = data['target']
        event_request = data['request']
    except Exception as e:
        print(e)
        return func.HttpResponse(
        "Exception Occured",status_code=400
    )

    # data parsing
    image_name = event_target['repository']
    image_tag = event_target['tag']
    image_size = event_target['size']
    image_digest = event_target['digest']
    container_registry = event_request['host']

    # request webhook to slack
    slack_webhook_url = "https://hooks.slack.com/services/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"
    slack_webhook_headers = {'Content-Type': 'application/json'}
    payload = \
    {
        "blocks": [
            {
                "type": "section",
                "fields": [
                    {
                        "type": "plain_text",
                        "text": f"[Event ID] \n {event_id}"
                    },
                    {
                        "type": "plain_text",
                        "text": f"[Event Time] \n {event_time}"
                    },
                    {
                        "type": "plain_text",
                        "text": f"[Event Action] \n {event_action}"
                    },
                    {
                        "type": "plain_text",
                        "text": f"[Image Name] \n {image_name}"
                    },
                    {
                        "type": "plain_text",
                        "text": f"[Image Tag] \n {image_tag}"
                    },
                    {
                        "type": "plain_text",
                        "text": f"[Image Size] \n {image_size}"
                    },
                    {
                        "type": "plain_text",
                        "text": f"[Image Digest] \n {image_digest}"
                    },
                    {
                        "type": "plain_text",
                        "text": f"[ACR] \n {container_registry}"
                    },
                    {
                        "type": "plain_text",
                        "text": f"[Image Full Name] \n {container_registry}/{image_name}:{image_tag}"
                    }
                ]
            }
        ]
    }
    slack_webhook_body = json.dumps(payload)
    
    try:
        response = requests.post(slack_webhook_url, data=slack_webhook_body, headers=slack_webhook_headers)
    except Exception as e:
        print(e)
        return func.HttpResponse(
        f"bad request",status_code=400
    )
    return func.HttpResponse(
        f"This HTTP triggered function executed successfully. response is -> {response}",status_code=response.status_code
    )
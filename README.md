# slack-webhook-python-func

Push Image --> ACR --> Webhook --> Function(HTTPTrigger) --> Webhook --> Slack Notification

### Environment
- Function
    - Python, Linux Type, HTTP Trigger, Authlevel=Anonymous
    - Required Python Package
        - azure-functions==1.17.0
        - requests==2.31.0
    - Required Tools
        - Azure Core tools installed in vscode extension

- ACR
    - Standard Tier

### Usage
1. 슬랙 봇의 웹훅 URL 입력
    ```
    slack_webhook_url = ""
    ```
2. Function App 배포

3. ACR 웹훅에 Function HTTP Trigger URL 입력

4. ACR에 이미지 Push

### Caution
- 슬랙 웹훅 URL은 깃헙같은 퍼블릭 저장소에 올릴경우 Disable됨 -> 404 에러 발생
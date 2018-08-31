from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('LskIi8K/5PbDDyW2AwPbqyOs2S9pz1ID/51dsOrxyJRAh2YhEpzU+/aZHdNelSconCXLJhi7fz2AAH8BnrI162fsz4Hg2RFBm6tIpxL11PzJNirDlPILj3wLWQLCxjpy88jaRTRqdwTla4NsQX4RjQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('580cbe76e5028f76cc1b7ad2e744362e')

@app.route("/callback", methods=['POST'])
def callback():
    print("callback")
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()

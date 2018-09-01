import os

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
    if not event.message.text.startswith("n!"):
        return
        
    message_content = event.message.text.split(" ")

    if message_content[0] == "n!say":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message_content[1])
        )
    


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

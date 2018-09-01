import os

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

from gag_core import Gag
from gag_core import Sections

app = Flask(__name__)
## LINE CLIENT
line_bot_api = LineBotApi(str( os.environ.get('LINE_ACCESS_TOKEN') ))
handler = WebhookHandler(str(os.environ.get('LINE_SECRET')))

## 9GAG CLIENT
gag_client = Gag()

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

    message_content = event.message.text.split(" ", 1)

    if message_content[0] == "n!say":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message_content[1])
        )
    
    elif message_content[0] == "n!lenny":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="( ͡° ͜ʖ ͡°)")
        )
    
    elif message_content[0] == "n!anime":
        post = gag_client.get_post_from(Sections.ANIME_MANGA)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=post.title)
        )
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=post.get_media_url(),
                preview_image_url=post.get_media_url()
            )
        )

    elif message_content[0] == "n!wtf":
        post = gag_client.get_post_from(Sections.WTF)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=post.title)
        )
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=post.get_media_url(),
                preview_image_url=post.get_media_url()
            )
        )

    elif message_content[0] == "n!kpop":
        post = gag_client.get_post_from(Sections.KPOP)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=post.title)
        )
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=post.get_media_url(),
                preview_image_url=post.get_media_url()
            )
        )

    elif message_content[0] == "n!savage":
        post = gag_client.get_post_from(Sections.SAVAGE)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=post.title)
        )
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=post.get_media_url(),
                preview_image_url=post.get_media_url()
            )
        )
    
    elif message_content[0] == "n!comic":
        post = gag_client.get_post_from(Sections.COMIC)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=post.title)
        )
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=post.get_media_url(),
                preview_image_url=post.get_media_url()
            )
        )
    


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

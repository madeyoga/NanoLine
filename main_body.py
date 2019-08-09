import os

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, VideoSendMessage
)

from ImageCore import Gag, Sections
from ImageCore import Reddit, Subreddits

import random

app = Flask(__name__)
## LINE CLIENT
line_bot_api = LineBotApi(str( os.environ.get('LINE_ACCESS_TOKEN') ))
handler = WebhookHandler(str(os.environ.get('LINE_SECRET')))

## 9GAG CLIENT
# gag_client = Gag()

## REDDIT CLIENT
reddit_client = Reddit()

@app.route("/callback", methods=['POST'])
def callback():
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

    if message_content[0] == "n!help":
        help_text = "Command List\nprefix: 'n!'"
        help_text += """
            Fun:
            - flip
            - rng     usage: n!rng 100
            Image:
            - tsun
            - scathach
            - illyasviel
            - raikou
            - fateprisma
            - fgo
            - fgoart
            - animeme
            - anime
            - waifu
            - meme
            - dank
            - wtf
            - azurlane
            - search   usage: n!search <keywords>
        """
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=help_text)
            )
    
    elif message_content[0] == "n!lenny":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="( ͡° ͜ʖ ͡°)")
        )

    elif message_content[0] == "n!scathach":
        submission = reddit_client.get_submission(Subreddits.SCATHACH)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )
    elif message_content[0] == "n!fgo":
        submission = reddit_client.get_submission(Subreddits.GRANDORDER)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )
        
    elif message_content[0] == "n!animeme":
        submission = reddit_client.get_submission(Subreddits.ANIMEMES)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )
    elif message_content[0] == "n!anime":
        submission = reddit_client.get_submission(Subreddits.ANIME)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )
        
    elif message_content[0] == "n!meme":
        submission = reddit_client.get_submission(Subreddits.MEMES)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )
        
    elif message_content[0] == "n!dank":
        submission = reddit_client.get_submission(Subreddits.DANKMEMES)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )
        
    elif message_content[0] == "n!wtf":
        submission = reddit_client.get_submission(Subreddits.WTF)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )
    elif message_content[0] == "n!waifu":
        submission = reddit_client.get_submission(Subreddits.WAIFU)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )
        
    elif message_content[0] == "n!fgoart":
        submission = reddit_client.get_submission(Subreddits.FGOFANART)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )
        
    elif message_content[0] == "n!azurlane":
        submission = reddit_client.get_submission(Subreddits.AZURELANE)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )

    elif message_content[0] == "n!illya":
        submission = reddit_client.get_submission(Subreddits.ILLYASVIEL)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )

    elif message_content[0] == "n!raikou":
        submission = reddit_client.get_submission(Subreddits.MAMARAIKOU)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )
    elif message_content[0] == "n!fgocomics":
        submission = reddit_client.get_submission(Subreddits.FGOCOMICS)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )
        
    elif message_content[0] == "n!fprisma":
        submission = reddit_client.get_submission(Subreddits.FATEPRISMAILLYA)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )
    elif message_content[0] == "n!saber":
        submission = reddit_client.get_submission(Subreddits.SABER)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )
    elif message_content[0] == "n!abby":
        submission = reddit_client.search_get_submission('all').search("fate abby")
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )
    elif message_content[0] == "n!flip":
        number = random.randint(0,2)
        if number == 0:
            text = "head"
        else:
            text = "tail"
            
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=text)
        )

    elif message_content[0] == "n!rng":
        number = random.randint(0, int(message_content[1]))
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(number))
        )
        
    elif message_content[0] == "n!search":
        submission = reddit_client.search_get_submission('all').search(message_content[1])
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=submission.url,
                preview_image_url=submission.url
            )
        )
        
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

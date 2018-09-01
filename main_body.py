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

from gag_core import Gag, Sections
from gag_core import Reddit, Subreddits

app = Flask(__name__)
## LINE CLIENT
line_bot_api = LineBotApi(str( os.environ.get('LINE_ACCESS_TOKEN') ))
handler = WebhookHandler(str(os.environ.get('LINE_SECRET')))

## 9GAG CLIENT
gag_client = Gag()

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
    
    elif message_content[0] == "n!lenny":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="( ͡° ͜ʖ ͡°)")
        )
    
    elif message_content[0] == "n!9anime":
        post = gag_client.get_post_from(Sections.ANIME_MANGA)
        if post.type == "Photo":
            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    original_content_url=post.get_media_url(),
                    preview_image_url=post.get_media_url()
                )
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                VideoSendMessage(
                    original_content_url=post.get_media_url()
                )
            )

    elif message_content[0] == "n!9wtf":
        post = gag_client.get_post_from(Sections.WTF)
        if post.type == "Photo":
            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    original_content_url=post.get_media_url(),
                    preview_image_url=post.get_media_url()
                )
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                VideoSendMessage(
                    original_content_url=post.get_media_url()
                )
            )

    elif message_content[0] == "n!9kpop":
        post = gag_client.get_post_from(Sections.KPOP)
        if post.type == "Photo":
            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    original_content_url=post.get_media_url(),
                    preview_image_url=post.get_media_url()
                )
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                VideoSendMessage(
                    original_content_url=post.get_media_url()
                )
            )

    elif message_content[0] == "n!9savage":
        post = gag_client.get_post_from(Sections.SAVAGE)
        if post.type == "Photo":
            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    original_content_url=post.get_media_url(),
                    preview_image_url=post.get_media_url()
                )
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                VideoSendMessage(
                    original_content_url=post.get_media_url()
                )
            )
    
    elif message_content[0] == "n!9comic":
        post = gag_client.get_post_from(Sections.COMIC)
        if post.type == "Photo":
            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    original_content_url=post.get_media_url(),
                    preview_image_url=post.get_media_url()
                )
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                VideoSendMessage(
                    original_content_url=post.get_media_url()
                )
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
    elif message_content[0] == "n!animemes":
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
        submission = reddit_client.get_submission(Subreddits.DANKMEMES)
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

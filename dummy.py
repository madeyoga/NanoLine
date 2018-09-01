from gag_core import Gag
from gag_core import Sections

import random

gag_client = Gag()

post = gag_client.get_post_from(Sections.COMIC)
print(post.title + " : " + post.get_media_url())

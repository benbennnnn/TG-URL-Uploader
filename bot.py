#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "AnyDLBot",
        bot_token=Config.6770770916:AAHhvXqWnKl1MYTe5GLJTIYGjn0kNRPlymY,
        api_id=Config.29051507,
        api_hash=Config.c3390b5ace39766d7c207a7cb8c3eee3,
        plugins=plugins
    )
    Config.AUTH_USERS.add(5975066452)
    app.run()

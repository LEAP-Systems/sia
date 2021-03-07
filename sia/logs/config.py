# -*- coding: utf-8 -*-
"""
Logger Config
=============
Modified: 2021-03

Copyright © 2021 LEAP Systems. All Rights Reserved.
"""

import logging.config
from pathlib import Path
import yaml

LOG_CONFIG_FILENAME = "config.yml"
CONFIG_PATH = Path(__file__).parent.joinpath(LOG_CONFIG_FILENAME)

def config():
    # bind logging to config file
    # verify path existance before initializing logger file configuration
    try:
        # load config from .yaml
        with open(CONFIG_PATH) as conf:
            logging.config.dictConfig(yaml.load(conf, Loader=yaml.FullLoader))
    except FileNotFoundError:
        print("Logging config file not found in expected absolute path: {}".format(CONFIG_PATH))
    except Exception as exc:
        print("Logging configuration failed: {}".format(exc))
    else:
        print("Logging configuration successful.")
#!/usr/bin/env python3

"""
It's just an example
"""

import webbrowser
import json

with open("service.settings.json", "r") as fp:
    settings = json.load(fp)

webbrowser.open(settings["url"], new=2)
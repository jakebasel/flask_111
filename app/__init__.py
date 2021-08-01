#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Simple flask app"""

from flask import Flask

app = Flask(__name__) # is a dunder variable or "magic variable"


@app.route("/")
def about_me(): # view funtion
    me ={
        "first_name":"Jake",
        "las_name":"Basel",
        "hobbies":"surf",
        "test":True,
    }
    return me



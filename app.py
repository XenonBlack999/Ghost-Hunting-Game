#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Dec 12 00:01:37 2025
@author: xenon
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

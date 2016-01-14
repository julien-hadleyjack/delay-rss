#!/usr/bin/env python3
# -- coding: utf-8 --

import datetime
from dateutil import parser, tz
from lxml import etree

from flask import Flask, request, abort, make_response, Response
from flask_appconfig import AppConfig
import requests


def create_app(configfile=None):
    app = Flask("delayrss")
    AppConfig(app, configfile)
    return app

app = create_app()


@app.route('/')
def delay_rss():
    url = request.args.get("url", "")
    timedelta = datetime.timedelta(
        minutes=int(request.args.get("minutes", "0")),
        hours=int(request.args.get("hours", "0")),
        days=int(request.args.get("days", "0")),
        weeks=int(request.args.get("weeks", "0"))
    )
    if not url:
        abort(make_response("Missing url parameter.", 400))
    if not timedelta:
        abort(make_response("Missing a timedelta parameter (minutes, hours, days and/or weeks).", 400))

    page = requests.get(request.args["url"])
    root = etree.fromstring(page.content, base_url=url)

    for article in root.xpath("//*[local-name() = 'item']"):
        date = article.xpath("./*[local-name() = 'date']/text()") or article.xpath("./*[local-name() = 'pubDate']/text()")
        pub_date = parser.parse(date[0])
        if pub_date + timedelta >= datetime.datetime.now(tz.tzlocal()):
            article.getparent().remove(article)

    return Response(etree.tostring(root), mimetype='text/xml')


if __name__ == '__main__':
    app.run(host=app.config.get("HOST", "127.0.0.1"), debug=app.config.get("DEBUG", False))

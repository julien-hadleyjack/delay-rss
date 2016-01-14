# Delay articles in a RSS feed

Delay articles in a RSS feed depending on the published date. If articles are behind a paywall for a certain period of time, you can use this web application to only show you articles you can read.

## Installation

This is a very simple flask application with a few dependencies.

### ... the manual way

To install the dependencies and start the application just run:

```shell
pip install -r requirements.txt
python delay-rss.py
```

It is recommended to isolate the dependencies by using something like [virtualenv](https://virtualenv.readthedocs.org/en/latest/) or  [conda](http://conda.pydata.org/docs/). See their documentation on how to do that.

### ... using docker-compose

The easiest way to get the application running is by using [docker-compose](https://docs.docker.com/compose/).

```shell
docker-compose build
docker-compose up -d && docker-compose logs
```

## Usage

If you start the application using the default settings, you should be able to see the text `Missing url parameter.` when you visit the URL <http://localhost:5000>. This means the application is up and running but you need to provide it with url parameters containing your data:

| Url Parameter | Mandatory |
|--------------:|:----------|
| url           | yes       |
| minutes       | no        |
| hours         | no        |
| days          | no        |
| weeks         | no        |

An example url could look like `http://localhost:5000/?url=http://feeds.feedburner.com/AndroidPolice%3Fformat=xml&hours=6` where articles have to be older than 6 hours.

## Configuration

To configure the flask application you can either:

* Point to the path a configuration file with the environment variable `GENRSS_CONFIG`
* Use the configuration options of [Flask](http://flask.pocoo.org/docs/latest/config/) as an environment variable with the prefix `GENRSS`.

You can for example use the environment variables `DELAYRSS_DEBUG=True` to enable debug mode or use `DELAYRSS_HOST=0.0.0.0` to make the application publicly accessable.

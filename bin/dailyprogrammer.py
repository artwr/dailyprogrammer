#!/usr/bin/env python3

import configparser
import logging
import os

import click
import praw
import requests

USER_AGENT = "Python:dailyprogrammer:v0.0.1 (by u/tittutur)"
CONFIG_LOCATION = "config/reddit.secret"
script_folder=os.path.dirname(os.path.abspath(__file__))
root_location=os.path.abspath(os.path.join(script_folder, os.path.pardir))

config = configparser.ConfigParser()
try:
    config.read(os.path.join(root_location,CONFIG_LOCATION))
    clientid=config["reddit-dailyprogrammer"]["clientid"]
    secret=config["reddit-dailyprogrammer"]["secret"]
except IOError:
    logging.error("Config file {} not found".format(CONFIG_LOCATION))
except KeyError as e:
    logging.error(e)



@click.command()
def cli():
    """
    Simple program that updates the directories up to the
    latest daily programmer challenge published on the subreddit
    """
    click.echo('I have updated to the lastest data!')



if __name__ == "__main__":
    cli()
    



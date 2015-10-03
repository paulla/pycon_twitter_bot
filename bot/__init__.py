# -*- coding: utf-8 -*-
import argparse
import ConfigParser

import twitter



def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('--conf',
                        help='conf file')

        args = parser.parse_args()

        config = ConfigParser.RawConfigParser()
        config.read(args.conf)

        api = twitter.Api(consumer_key=config.get('twitter', 'consumer_key'),
                          consumer_secret=config.get('twitter', 'consumer_secret'),
                          access_token_key=config.get('twitter', 'access_token_key'),
                          access_token_secret=config.get('twitter', 'access_token_secret'))
        print api.VerifyCredentials()

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

        api = twitter.Api(consumer_key='consumer_key',
                          consumer_secret='consumer_secret',
                          access_token_key='access_token',
                          access_token_secret='access_token_secret')
        print api.VerifyCredentials()

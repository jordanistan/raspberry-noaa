#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import tweepy

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN_KEY = os.environ['ACCESS_TOKEN_KEY']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
argentinaFlag = u'\U0001F1E6' + u'\U0001F1F7'

filenames = []
for element in sys.argv[3:]:
  filenames.append(element)

media_ids = []
for filename in filenames:
  res = api.media_upload(filename)
  media_ids.append(res.media_id)

api.update_status(status=argentinaFlag + ' Imagen satelital: ' + sys.argv[1] + '. Elevacion maxima: ' + sys.argv[2] + ' grados. #NOAA #weather #argentinaimagenes #noaasatellite #clima #wxtoimg #raspberrynoaa #argentina #argentinasat', media_ids=media_ids)

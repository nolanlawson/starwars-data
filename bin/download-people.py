#!/usr/bin/env python

import requests;
import re;
import string;
import json;

for i in range(1, 88):
#for i in range(1, 2):
  url = 'http://swapi.co/api/people/%d' % (i)
  response = requests.get(url)
  if response.status_code != 200:
    continue
  person = requests.get(url).json()
  name = person['name'].replace(' ', '_')
  print "downloading", name
  page = requests.get('http://starwars.wikia.com/wiki/%s' % name).text
  did_you_mean = re.findall('Did you mean <a href="([^"]+)"', page)
  if len(did_you_mean) > 0:
    page = requests.get('http://starwars.wikia.com%s' % did_you_mean[0]).text
  img =  re.findall('"([^"]+)" class="pi-image-thumbnail"', page)
  if len(img) == 0:
    continue
  fileout = open('person_' + str(i) + '.json', 'w');
  fileout.write(json.dumps(person, sort_keys=True, indent=2, separators=(',', ': ')))
  fileout.close()
  img_data = requests.get(img[0], stream=True)
  with open('person_' + str(i) + '.png', 'wb') as fd:
    for chunk in img_data.iter_content(0x100000):
      fd.write(chunk)
  
  

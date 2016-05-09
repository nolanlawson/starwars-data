#!/usr/bin/env python

import json

list = []

for i in range(0, 100):
  try:
    filein = open('person_' + str(i) + '.json', 'r')
    person = json.loads(filein.read())
    person['id'] = i
    filein.close()
    list.append(person)
  except:
    pass

print json.dumps(list, sort_keys=True, indent=2, separators=(',', ': '))

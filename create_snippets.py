#!/usr/bin/env python3

import json
import re
import requests
import time
import datetime
from bs4 import BeautifulSoup

Qt_version = '5.12'
Qt_url_prefix = 'https://doc.qt.io/qt-' + Qt_version + '/'

request  = requests.get(Qt_url_prefix + 'qmltypes.html')
soup = BeautifulSoup(request.text, 'html.parser')

# Get all types and reference link
types = {}
for link in soup.find_all('dd'):
    if link is not None:
        types[link.a.text.split(' ')[0].replace(':', '')] = {'member_link': Qt_url_prefix + link.a.get('href')[:-5] + '-members.html'}

# Get function, variables and signals of all types
processed_items = 1
total_number_of_items = len(types)
started_time = time.time()
for name in types.keys():
#    if str(name) not in 'Component':
#        continue
    #print('yep!!!')
    request  = requests.get(types[name]['member_link'])
    soup = BeautifulSoup(request.text, 'html.parser')
    types[name]['all'] = []
    for val in soup.find_all('li', class_="fn"):
        types[name]['all'] += [val.text]

    wait_time = ((time.time() - started_time)/processed_items)*(total_number_of_items - processed_items)
    print(name, '\t', str(datetime.timedelta(seconds=wait_time)))
    processed_items += 1
    #break

# Populate dict
final_dict = eval(open("manual_snippets.json").read())
dict_template = \
'''
    \"{name}\": {
        \"body\": \"{name} {\n    {body}\n}\",
        \"description\": \"{description}\",
        \"prefix\": \"{name}\",
        \"scope\": \"source.qml\"
    },
'''

for name in types.keys():
    print(name)
    #if 'all' not in types[name]:
    #    continue

    types[name]['list'] = []
    for member in types[name]['all']:
        if '[attached]' in member:
            types[name]['signal'] =  '//on' + member.title()[:-len('() [attached]')] + ': { }'
            types[name]['list'] += [types[name]['signal']]
        elif re.match('^\w*\ \w*\(.*\)$', member):
            types[name]['function'] = member
        else:
            types[name]['variable'] = '//' + member.replace(' ', '').replace(':', ': ')
            types[name]['list'] += [types[name]['variable']]

    #print(types[name]['list'])
    final_dict[name] = \
    {
        "prefix": name,
        "body": name + '{\n    %s\n}' % (('\n    ').join(types[name]['list'])),
        "description": name,
        "scope": "source.qml"
    }

print(json.dumps(final_dict, sort_keys=True, indent=4))

f = open('output.json','w')
f.write(json.dumps(final_dict, sort_keys=True, indent=4))
f.close()

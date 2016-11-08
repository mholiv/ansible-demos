#!/usr/bin/env python
import json

data = {}

data['webservers'] = {}

data['webservers']['hosts'] = ['10.0.0.1', '10.0.0.2']
data['webservers']['vars'] = {'a': True}

data['_meta'] = {}
data['_meta']['hostvars'] = {'10.0.0.1':{'b': False}}

print json.dumps(data, indent=2)

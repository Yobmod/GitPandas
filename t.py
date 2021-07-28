from typing import Any, Dict, List, Union
import urllib.request
import json
import requests
import pprint

GithubJson = Dict[str,
                  Union[str, int, bool, None, Dict[str,
                                                   Union[str, int, bool, None, Dict]]]]


name = 'yobmod'
uri = f'https://api.github.com/users/{name}/repos'

req = urllib.request.Request(uri)
with urllib.request.urlopen(req) as response:
    content: bytes = response.read()
    jresp: GithubJson = json.loads(content)
    pprint.pprint(jresp)
    print(len(content))

# data = requests.get(uri)
# content = data.content
# print(data.json())
# print(len(content))

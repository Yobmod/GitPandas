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

"""
 [{'archive_url': 'https://api.github.com/repos/Yobmod/DnD4py/{archive_format}{/ref}',
  'archived': False,
  'assignees_url': 'https://api.github.com/repos/Yobmod/DnD4py/assignees{/user}',
  'blobs_url': 'https://api.github.com/repos/Yobmod/DnD4py/git/blobs{/sha}',
  'branches_url': 'https://api.github.com/repos/Yobmod/DnD4py/branches{/branch}',
  'clone_url': 'https://github.com/Yobmod/DnD4py.git',
  'collaborators_url': 'https://api.github.com/repos/Yobmod/DnD4py/collaborators{/collaborator}',
  'comments_url': 'https://api.github.com/repos/Yobmod/DnD4py/comments{/number}',
  'commits_url': 'https://api.github.com/repos/Yobmod/DnD4py/commits{/sha}',
  'compare_url': 'https://api.github.com/repos/Yobmod/DnD4py/compare/{base}...{head}',
  'contents_url': 'https://api.github.com/repos/Yobmod/DnD4py/contents/{+path}',
  'contributors_url': 'https://api.github.com/repos/Yobmod/DnD4py/contributors',
  'created_at': '2020-06-13T00:02:53Z',
  'default_branch': 'master',
  'deployments_url': 'https://api.github.com/repos/Yobmod/DnD4py/deployments',
  'description': 'Python utilities for D&D (5th Edition)',
  'disabled': False,
  'downloads_url': 'https://api.github.com/repos/Yobmod/DnD4py/downloads',
  'events_url': 'https://api.github.com/repos/Yobmod/DnD4py/events',
  'fork': True,
  'forks': 0,
  'forks_count': 0,
  'forks_url': 'https://api.github.com/repos/Yobmod/DnD4py/forks',
  'full_name': 'Yobmod/DnD4py',
  'git_commits_url': 'https://api.github.com/repos/Yobmod/DnD4py/git/commits{/sha}',
  'git_refs_url': 'https://api.github.com/repos/Yobmod/DnD4py/git/refs{/sha}',
  'git_tags_url': 'https://api.github.com/repos/Yobmod/DnD4py/git/tags{/sha}',
  'git_url': 'git://github.com/Yobmod/DnD4py.git',
  'has_downloads': True,
  'has_issues': False,
  'has_pages': False,
  'has_projects': True,
  'has_wiki': True,
  'homepage': None,
  'hooks_url': 'https://api.github.com/repos/Yobmod/DnD4py/hooks',
  'html_url': 'https://github.com/Yobmod/DnD4py',
  'id': 271910965,
  'issue_comment_url': 'https://api.github.com/repos/Yobmod/DnD4py/issues/comments{/number}',
  'issue_events_url': 'https://api.github.com/repos/Yobmod/DnD4py/issues/events{/number}',
  'issues_url': 'https://api.github.com/repos/Yobmod/DnD4py/issues{/number}',
  'keys_url': 'https://api.github.com/repos/Yobmod/DnD4py/keys{/key_id}',
  'labels_url': 'https://api.github.com/repos/Yobmod/DnD4py/labels{/name}',
  'language': None,
  'languages_url': 'https://api.github.com/repos/Yobmod/DnD4py/languages',
  'license': {'key': 'mit',
              'name': 'MIT License',
              'node_id': 'MDc6TGljZW5zZTEz',
              'spdx_id': 'MIT',
              'url': 'https://api.github.com/licenses/mit'},
  'merges_url': 'https://api.github.com/repos/Yobmod/DnD4py/merges',
  'milestones_url': 'https://api.github.com/repos/Yobmod/DnD4py/milestones{/number}',
  'mirror_url': None,
  'name': 'DnD4py',
  'node_id': 'MDEwOlJlcG9zaXRvcnkyNzE5MTA5NjU=',
  'notifications_url': 'https://api.github.com/repos/Yobmod/DnD4py/notifications{?since,all,participating}',
  'open_issues': 0,
  'open_issues_count': 0,
  'owner': {'avatar_url': 'https://avatars.githubusercontent.com/u/22235459?v=4',
            'events_url': 'https://api.github.com/users/Yobmod/events{/privacy}',
            'followers_url': 'https://api.github.com/users/Yobmod/followers',
            'following_url': 'https://api.github.com/users/Yobmod/following{/other_user}',
            'gists_url': 'https://api.github.com/users/Yobmod/gists{/gist_id}',
            'gravatar_id': '',
            'html_url': 'https://github.com/Yobmod',
            'id': 22235459,
            'login': 'Yobmod',
            'node_id': 'MDQ6VXNlcjIyMjM1NDU5',
            'organizations_url': 'https://api.github.com/users/Yobmod/orgs',
            'received_events_url': 'https://api.github.com/users/Yobmod/received_events',
            'repos_url': 'https://api.github.com/users/Yobmod/repos',
            'site_admin': False,
            'starred_url': 'https://api.github.com/users/Yobmod/starred{/owner}{/repo}',
            'subscriptions_url': 'https://api.github.com/users/Yobmod/subscriptions',
            'type': 'User',
            'url': 'https://api.github.com/users/Yobmod'},
  'private': False,
  'pulls_url': 'https://api.github.com/repos/Yobmod/DnD4py/pulls{/number}',
  'pushed_at': '2019-03-21T20:33:12Z',
  'releases_url': 'https://api.github.com/repos/Yobmod/DnD4py/releases{/id}',
  'size': 25,
  'ssh_url': 'git@github.com:Yobmod/DnD4py.git',
  'stargazers_count': 0,
  'stargazers_url': 'https://api.github.com/repos/Yobmod/DnD4py/stargazers',
  'statuses_url': 'https://api.github.com/repos/Yobmod/DnD4py/statuses/{sha}',
  'subscribers_url': 'https://api.github.com/repos/Yobmod/DnD4py/subscribers',
  'subscription_url': 'https://api.github.com/repos/Yobmod/DnD4py/subscription',
  'svn_url': 'https://github.com/Yobmod/DnD4py',
  'tags_url': 'https://api.github.com/repos/Yobmod/DnD4py/tags',
  'teams_url': 'https://api.github.com/repos/Yobmod/DnD4py/teams',
  'trees_url': 'https://api.github.com/repos/Yobmod/DnD4py/git/trees{/sha}',
  'updated_at': '2020-06-13T00:02:55Z',
  'url': 'https://api.github.com/repos/Yobmod/DnD4py',
  'watchers': 0,
  'watchers_count': 0},]
"""

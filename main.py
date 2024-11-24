#%%
from os import environ
from time import sleep
from atproto import Client
from math import ceil
#%%
client = Client()
profile = client.login(environ['BSKY_ID'], environ['BSKY_PASS'])
#%%
follows = []
cursor = None
for i in range(ceil(profile.follows_count/100)):
    res = client.get_follows(profile.did, cursor, 100)
    for j in res.follows:
        follows.append(j.did)
    cursor = res.cursor
#%%
followers = []
cursor = None
for i in range(ceil(profile.followers_count/100)):
    res = client.get_followers(profile.did, cursor, 100)
    for j in res.followers:
        followers.append(j.did)
    cursor = res.cursor
#%%
follows = set(follows)
followers = set(followers)
not_following_me = follows - followers
not_followed_by_me = followers - follows
#%%
for i in not_followed_by_me:
    client.follow(i)
#%%
for i in not_following_me:
    client.unfollow(i)
    sleep(1)
    client.follow(i)
    sleep(1)
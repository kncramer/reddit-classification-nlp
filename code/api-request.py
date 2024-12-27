# imports
import pandas as pd
import requests
import time
import datetime
import getpass


# prompt and store login credentials to access API
client_id = getpass.getpass(prompt="Client ID: ")
client_secret = getpass.getpass(prompt="Client Secret: ")
user_agent = getpass.getpass(prompt="User Agent: ")
username = getpass.getpass(prompt="Username: ")
password = getpass.getpass(prompt="Password: ")



# authorize access
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

data = {
    "grant_type": "password",
    "username": username,
    "password": password
}

# create header for application
headers = {"User-Agent": "dsb826/0.0.1"}

res = requests.post(
    "https://www.reddit.com/api/v1/access_token",
    auth=auth,
    data=data,
    headers=headers)

# confirm access
print(f"Response status: {res}")

# store access token
token = res.json()["access_token"]

# add access token header
headers["Authorization"] = f"bearer {token}"

# set up base url and collect subreddits of interest
base_url = "https://oauth.reddit.com/r/"
subreddit1 = input("First Subreddit: ").lower().strip()
subreddit2 = input("Second Subreddit: ").lower().strip()



# getting 1000 newest posts from first subreddit
# start with first 100
params = {
    "limit": 100,
}
res_1 = requests.get(base_url+subreddit1+"/new", headers=headers, params=params)

# extract titles and posts from response object and store in dataframe
titles_1 = [post["data"]["title"] for post in res_1.json()["data"]["children"]]
posts_1 = [post["data"]["selftext"] for post in res_1.json()["data"]["children"]]
df_1 = pd.DataFrame({"title": titles_1, "post": posts_1})

# set first after parameter
after = res_1.json()["data"]["after"]



# now loop to get the next 900
for _ in range(9):
    params = {
        "limit": 100,
        "after": after
    }

    res_1 = requests.get(base_url+subreddit1+"/new", headers=headers, params=params)

    # extract titles and posts from response object and add to subreddit1 dataframe
    titles_1 = [post["data"]["title"] for post in res_1.json()["data"]["children"]]
    posts_1 = [post["data"]["selftext"] for post in res_1.json()["data"]["children"]]
    df_1 = pd.concat((df_1, pd.DataFrame({"title": titles_1, "post": posts_1})))

    # set starting point for next loop iteration
    after = res_1.json()["data"]["after"]

    # pause the loop
    time.sleep(5)



# collecting 1000 of the hottest posts
# start with first 100 hottest posts
params = {
    "limit": 100,
}
res_1 = requests.get(base_url+subreddit1+"/hot", headers=headers, params=params)

# extract titles and posts from response object and add to subreddit1 dataframe
titles_1 = [post["data"]["title"] for post in res_1.json()["data"]["children"]]
posts_1 = [post["data"]["selftext"] for post in res_1.json()["data"]["children"]]
df_1 = pd.concat((df_1, pd.DataFrame({"title": titles_1, "post": posts_1})))

# set first after parameter
after = res_1.json()["data"]["after"]



# loop through next 900 hottest posts
for _ in range(10):
    params = {
        "limit": 100,
        "after": after
    }

    res_1 = requests.get(base_url+subreddit1+"/hot", headers=headers, params=params)

    # extract titles and posts from response object and add to subreddit1 dataframe
    titles_1 = [post["data"]["title"] for post in res_1.json()["data"]["children"]]
    posts_1 = [post["data"]["selftext"] for post in res_1.json()["data"]["children"]]
    df_1 = pd.concat((df_1, pd.DataFrame({"title": titles_1, "post": posts_1})))

    # set starting point for next loop iteration
    after = res_1.json()["data"]["after"]

    # pause the loop
    time.sleep(5)



# drop any duplicates between new and hot posts
df_1 = df_1.drop_duplicates()


# create column with subreddit name
df_1["subreddit"] = subreddit1



# reading in any previously collected data to drop duplicates before saving new data to file
try:
    old_df_1 = pd.read_csv("../data/subreddit1-data.csv")
except FileNotFoundError:  # for first run through when this file doesn't exist yet
    pass

# combine previous data with new
# method to verify dataframe existence found using Google AI
if isinstance(old_df_1, pd.DataFrame):
    new_df_1 = pd.concat((old_df_1, df_1))

# drop any duplicates between new and any previous data collection
if isinstance(new_df_1, pd.DataFrame):
    new_df_1 = new_df_1.drop_duplicates()



# save first subreddit data to csv
if isinstance(new_df_1, pd.DataFrame):
    new_df_1.to_csv("../data/subreddit1-data.csv", index=False)
else:
    df_1.to_csv("../data/subreddit1-data.csv", index=False) # for first run through




# getting 1000 newest posts for second subreddit
# start with first 100
params = {
    "limit": 100,
}
res_2 = requests.get(base_url+subreddit2+"/new", headers=headers, params=params)

# extract titles and posts from response object and store in dataframe
titles_2 = [post["data"]["title"] for post in res_2.json()["data"]["children"]]
posts_2 = [post["data"]["selftext"] for post in res_2.json()["data"]["children"]]
df_2 = pd.DataFrame({"title": titles_2, "post": posts_2})

# set first after parameter
after = res_2.json()["data"]["after"]



# now loop to get the next 900
for _ in range(9):
    params = {
        "limit": 100,
        "after": after
    }

    res_2 = requests.get(base_url+subreddit2+"/new", headers=headers, params=params)

    # extract titles and posts from response object and add to subreddit2 dataframe
    titles_2 = [post["data"]["title"] for post in res_2.json()["data"]["children"]]
    posts_2 = [post["data"]["selftext"] for post in res_2.json()["data"]["children"]]
    df_2 = pd.concat((df_2, pd.DataFrame({"title": titles_2, "post": posts_2})))

    # set starting point for next loop iteration
    after = res_2.json()["data"]["after"]

    # pause the loop
    time.sleep(5)



# collecting 1000 hottest posts
# starting with first 100 hottest posts
params = {
    "limit": 100,
}
res_2 = requests.get(base_url+subreddit2+"/hot", headers=headers, params=params)

# extract titles and posts from response object and add to subreddit2 dataframe
titles_2 = [post["data"]["title"] for post in res_2.json()["data"]["children"]]
posts_2 = [post["data"]["selftext"] for post in res_2.json()["data"]["children"]]
df_2 = pd.concat((df_2, pd.DataFrame({"title": titles_2, "post": posts_2})))

# set first after parameter
after = res_2.json()["data"]["after"]



# loop through next 900 hottest posts
for _ in range(9):
    params = {
        "limit": 100,
        "after": after
    }

    res_2 = requests.get(base_url+subreddit2+"/hot", headers=headers, params=params)

    # extract titles and posts from response object and add to subreddit2 dataframe
    titles_2 = [post["data"]["title"] for post in res_2.json()["data"]["children"]]
    posts_2 = [post["data"]["selftext"] for post in res_2.json()["data"]["children"]]
    df_2 = pd.concat((df_2, pd.DataFrame({"title": titles_2, "post": posts_2})))

    # set starting point for next loop iteration
    after = res_2.json()["data"]["after"]

    # pause the loop
    time.sleep(5)
    


# drop any duplicates collected between new and hot posts
df_2 = df_2.drop_duplicates()

# create column with subreddit name
df_2["subreddit"] = subreddit2



# reading in any previously collected data to drop duplicates before saving new data to file
try:
    old_df_2 = pd.read_csv("../data/subreddit2-data.csv")
except FileNotFoundError:  # for first run through when this file doesn't exist yet
    pass

# combine previous data with new
if isinstance(old_df_2, pd.DataFrame):
    new_df_2 = pd.concat((old_df_2, df_2))

# drop any duplicates between new and any previous data collection
if isinstance(new_df_2, pd.DataFrame):
    new_df_2 = new_df_2.drop_duplicates()



# save second subreddit data to csv
if isinstance(new_df_2, pd.DataFrame):
    new_df_2.to_csv("../data/subreddit2-data.csv", index=False)
else:
    df_2.to_csv("../data/subreddit2-data.csv", index=False) # for first run through



# record date/time and size of data collection
time_stamp = datetime.datetime.now()
f = open("../data/time-stamps.txt", "a")  # open file and append
f.write(f"Data collected {time_stamp:%b %d, %Y} at {time_stamp:%H:%M}\n")  # extract details of time stamp
f.write(f"\t{df_1.shape[0]} posts from {subreddit1} subreddit\n")
f.write(f"\t{df_2.shape[0]} posts from {subreddit2} subreddit\n\n")
f.close()
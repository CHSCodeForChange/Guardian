from tweepy import OAuthHandler
import tweepy

import twitter_creds

class UserManager:
    auth = None
    api = None


    def __init__(self):
        self.auth = OAuthHandler(twitter_creds.CONSUMER_KEY, twitter_creds.CONSUMER_SECRET)
        self.auth.set_access_token(twitter_creds.ACCESS_TOKEN, twitter_creds.ACCESS_TOKEN_SECRET)

        self.api = tweepy.API(self.auth)

    def get_api (self):
        return self.api

    def get_users_by_root_user(self, root_user, layers):
        users = root_user
        for i in range(0,layers):
            if users != root_user:
                for user in users:
                    users = users + user.friends()
            else:
                users = root_user.friends()

        return users


if __name__ == "__main__":
    mgr = UserManager()
    root_user = mgr.get_api().get_user('CHSCodeChange')
    users = mgr.get_users_by_root_user(root_user, 2)

    for user in users:
        print (user.screen_name)




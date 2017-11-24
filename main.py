import tweepy


from logincredentials import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

list=[]

person= input('Enter the twitter handle you wish to search (0 to exit): ')

while person != 0:

    user = api.get_user(person)
    tweets= int(input('Enter your tweet requirements: '))
    followers= int(input('Enter your follower requirements: '))


    print("Users informatios: \n\n\nName:", user.name)
    print("Twitter Handle: ", user.id_str)
    print("Description: ", user.description)
    print("Location:",user.location)
    print("Number of people Following: ",user.friends_count)
    print("Number of Followers: ",user.followers_count)
    print("Number of Tweets: ", str(user.statuses_count))
    print("\n")


    if user.followers_count>followers and user.statuses_count>tweets:
    #api.update_status(status="VALID")
        list.append(user.name)
        print("Updated list of valid users is: \n", list)


    else:
        print("\n\nInvalid User")
    person= input('Enter the twitter handle you wish to search (0 to exit): ')

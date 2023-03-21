import requests
import time
import colorama
from colorama import Fore, Style, Back

colorama.init()

sessionid = input("[I] Enter Sessionid : ")
user = input("[I] Enter Username : ")

headers = {
    "Host": "i.instagram.com",
    "Accept": "*/*",
    "User-Agent": "Instagram 118.0.0.25.121 (iPhone11,8; iOS 13_1_3; en_US; en-US; scale=2.00; 828x1792; 180988914)",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": f"sessionid={sessionid}"
}


def getid():
    id = requests.get(f"https://i.instagram.com/api/v1/users/{user}/usernameinfo/", headers=headers).json()
    try:
        return id["user"]["pk"]
    except KeyError:
        print(f"    {Back.RED} Error: {id['message']} {Back.RESET}")
        exit()


def getStories():
    stories = (requests.get(f"https://i.instagram.com/api/v1/feed/user/{getid()}/story/", headers=headers)).json()
    return [story['pk'] for story in stories['reel']['items']]


def getViewers(story_id):

    viewers = (requests.get(f"https://i.instagram.com/api/v1/media/{story_id}/list_reel_media_viewer/", headers=headers)).json()
    return [viewer['username'] for viewer in viewers['users']]

for story in getStories():

    print(f"Story {Fore.YELLOW + str(story) + Fore.RESET} | Viewers: {Fore.GREEN}{', '.join(getViewers(story))}{Fore.RESET}")
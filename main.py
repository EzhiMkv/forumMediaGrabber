import requests
from bs4 import BeautifulSoup
import mpv

print('pew')

# оставь для музла этот божественный скрипт
x = requests.get('https://boards.4channel.org/wsg/thread/4791588')
print(x.status_code)

soup = BeautifulSoup(x.content, features="html.parser")
links = soup.find_all('a')

playlist_filepath = 'playlist.m3u'


def check_exists(link_to_check):
    with open(playlist_filepath, 'r') as fp:
        lines = fp.readlines()
        for row in lines:
            if row.find(link_to_check) != -1:
                return True
        return False


for link in links:
    stuff_link = link['href']
    if stuff_link.endswith(".webm"):
        if not check_exists(stuff_link):
            print(stuff_link)
            playlist_file = open(playlist_filepath, 'a+')
            playlist_file.write("https:"+stuff_link+"\n")
            playlist_file.close()


def my_log(loglevel, component, message):
    print('[{}] {}: {}'.format(loglevel, component, message))


player = mpv.MPV(ytdl=True,
                 input_default_bindings=True,
                 input_vo_keyboard=True,
                 osc=True,
                 loop='inf',
                 log_handler=my_log,
                 loglevel='debug'
                 )
player.loadlist(playlist_filepath)
player.playlist_shuffle()
player.playlist_pos = 0
player['vo'] = 'gpu'

# player.wait_for_playback()
player.wait_for_shutdown()



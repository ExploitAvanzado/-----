
# -*- coding: utf-8 -*-
#!/usr/bin/python3
import sys
import os
import requests
import time
import socket
import random
from time import sleep
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
def print_slow(txt):
    for x in txt:                     # cycle through the text one character at a time
        print(x, end='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.1)
    print() # go to new line
#Login
os.system('cls')
contador = 1
while contador <= 3:
    usuario = input("\033[92m[-] User [-]  :")
    contraseña = input("\033[92m[-] Password [-]  :")
    if usuario == "Lmao" and contraseña == "Lmao":
        contador = 4
        print('''
        \033c        
        
                   \033[92m ┌─ ─┐  ╦  ╔═╗╔═╗╔═╗╦╔╗╔  ┌─ ─┐
                  \033[92m  │───│  ║  ║ ║║ ╦║ ╦║║║║  │───│
                  \033[92m  └─ ─┘  ╩═╝╚═╝╚═╝╚═╝╩╝╚╝  └─ ─┘
''')
    else:
        print('''
        \033c
                  \033[91m ┌─ ─┐  ╦═╗╔═╗╔╦╗╦═╗╦ ╦       ┌─ ─┐
                  \033[91m │───│  ╠╦╝║╣  ║ ╠╦╝╚╦╝       │───│
                  \033[91m └─ ─┘  ╩╚═╚═╝ ╩ ╩╚═ ╩   ooo  └─ ─┘

        ''')
        time.sleep(5)
        os.system('clear')#linux  #windows ('cls')
        if contador == 3:
            contador = contador +1
time.sleep(5)
os.system('clear')#linux('clear')  #windows ('cls')
''' INPUT USERNMAE TO DOX '''
username = input('\033[92m{+} Enter username to DOX: ')


# INSTAGRAM
instagram = f'https://www.instagram.com/{username}'

# FACEBOOK
facebook = f'https://www.facebook.com/{username}'

#TWITTER
twitter = f'https://www.twitter.com/{username}'

# YOUTUBE
youtube = f'https://www.youtube.com/{username}'

# BLOGGER
blogger = f'https://{username}.blogspot.com'

# GOOGLE+
google_plus = f'https://plus.google.com/s/{username}/top'

# REDDIT
reddit = f'https://www.reddit.com/user/{username}'

# WORDPRESS
wordpress = f'https://{username}.wordpress.com'

# PINTEREST
pinterest = f'https://www.pinterest.com/{username}'

# GITHUB
github = f'https://www.github.com/{username}'

# TUMBLR
tumblr = f'https://{username}.tumblr.com'

# FLICKR
flickr = f'https://www.flickr.com/people/{username}'

# STEAM
steam = f'https://steamcommunity.com/id/{username}'

# VIMEO
vimeo = f'https://vimeo.com/{username}'

# SOUNDCLOUD
soundcloud = f'https://soundcloud.com/{username}'

# DISQUS
disqus = f'https://disqus.com/by/{username}'

# MEDIUM
medium = f'https://medium.com/@{username}'

# DEVIANTART
deviantart = f'https://{username}.deviantart.com'

# VK
vk = f'https://vk.com/{username}'

# ABOUT.ME
aboutme = f'https://about.me/{username}'

# IMGUR
imgur = f'https://imgur.com/user/{username}'

# FLIPBOARD
flipboard = f'https://flipboard.com/@{username}'

# SLIDESHARE
slideshare = f'https://slideshare.net/{username}'

# FOTOLOG
fotolog = f'https://fotolog.com/{username}'

# SPOTIFY
spotify = f'https://open.spotify.com/user/{username}'

# MIXCLOUD
mixcloud = f'https://www.mixcloud.com/{username}'

# SCRIBD
scribd = f'https://www.scribd.com/{username}'

# BADOO
badoo = f'https://www.badoo.com/en/{username}'

# PATREON
patreon = f'https://www.patreon.com/{username}'

# BITBUCKET
bitbucket = f'https://bitbucket.org/{username}'

# DAILYMOTION
dailymotion = f'https://www.dailymotion.com/{username}'

# ETSY
etsy = f'https://www.etsy.com/shop/{username}'

# CASHME
cashme = f'https://cash.me/{username}'

# BEHANCE
behance = f'https://www.behance.net/{username}'

# GOODREADS
goodreads = f'https://www.goodreads.com/{username}'

# INSTRUCTABLES
instructables = f'https://www.instructables.com/member/{username}'

# KEYBASE
keybase = f'https://keybase.io/{username}'

# KONGREGATE
kongregate = f'https://kongregate.com/accounts/{username}'

# LIVEJOURNAL
livejournal = f'https://{username}.livejournal.com'

# ANGELLIST
angellist = f'https://angel.co/{username}'

# LAST.FM
last_fm = f'https://last.fm/user/{username}'

# DRIBBBLE
dribbble = f'https://dribbble.com/{username}'

# CODECADEMY
codecademy = f'https://www.codecademy.com/{username}'

# GRAVATAR
gravatar = f'https://en.gravatar.com/{username}'

# PASTEBIN
pastebin = f'https://pastebin.com/u/{username}'

# FOURSQUARE
foursquare = f'https://foursquare.com/{username}'

# ROBLOX
roblox = f'https://www.roblox.com/user.aspx?username={username}'

# GUMROAD
gumroad = f'https://www.gumroad.com/{username}'

# NEWSGROUND
newsground = f'https://{username}.newgrounds.com'

# WATTPAD
wattpad = f'https://www.wattpad.com/user/{username}'

# CANVA
canva = f'https://www.canva.com/{username}'

# CREATIVEMARKET
creative_market = f'https://creativemarket.com/{username}'

# TRAKT
trakt = f'https://www.trakt.tv/users/{username}'

# 500PX
five_hundred_px = f'https://500px.com/{username}'

# BUZZFEED
buzzfeed = f'https://buzzfeed.com/{username}'

# TRIPADVISOR
tripadvisor = f'https://tripadvisor.com/members/{username}'

# HUBPAGES
hubpages = f'https://{username}.hubpages.com'

# CONTENTLY
contently = f'https://{username}.contently.com'

# HOUZZ
houzz = f'https://houzz.com/user/{username}'

#BLIP.FM
blipfm = f'https://blip.fm/{username}'

# WIKIPEDIA
wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'

# HACKERNEWS
hackernews = f'https://news.ycombinator.com/user?id={username}'

# CODEMENTOR
codementor = f'https://www.codementor.io/{username}'

# REVERBNATION
reverb_nation = f'https://www.reverbnation.com/{username}'

# DESIGNSPIRATION
designspiration = f'https://www.designspiration.net/{username}'

# BANDCAMP
bandcamp = f'https://www.bandcamp.com/{username}'

# COLOURLOVERS
colourlovers = f'https://www.colourlovers.com/love/{username}'

# IFTTT
ifttt = f'https://www.ifttt.com/p/{username}'

# EBAY
ebay = f'https://www.ebay.com/usr/{username}'

''' WEBSITE LIST - USE FOR SEARCHING OF USERNAME '''
WEBSITES = [
instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus, 
medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
bandcamp, colourlovers, ifttt, ebay,
]


''' COLOUR PRINTING FUNCTION '''
def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')
    return inner_function


''' COLOUR PRINTS '''
GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[91m')


''' BANNER '''
def banner():
    YELLOW(r'''
 `7MM"""Yb.                                                       `7MM                        `7MM      `7MMF'                                              
   MM    `Yb.                                                       MM                          MM        MM                                                
   MM     `Mb  ,pW"Wq.`7M'   `MF'.gP"Ya   ,6"Yb.  `7MMpMMMb.   ,M""bMM  ,pW"Wq.       ,6"Yb.    MM        MM        `7MMpMMMb.pMMMb.   ,6"Yb.  ,pW"Wq.      
   MM      MM 6W'   `Wb `VA ,V' ,M'   Yb 8)   MM    MM    MM ,AP    MM 6W'   `Wb     8)   MM    MM        MM          MM    MM    MM  8)   MM 6W'   `Wb     
   MM     ,MP 8M     M8   XMX   8M""""""  ,pm9MM    MM    MM 8MI    MM 8M     M8      ,pm9MM    MM        MM      ,   MM    MM    MM   ,pm9MM 8M     M8     
   MM    ,dP' YA.   ,A9 ,V' VA. YM.    , 8M   MM    MM    MM `Mb    MM YA.   ,A9     8M   MM    MM        MM     ,M   MM    MM    MM  8M   MM YA.   ,A9     
 .JMMmmmdP'    `Ybmd9'.AM.   .MA.`Mbmmd' `Moo9^Yo..JMML  JMML.`Wbmd"MML.`Ybmd9'      `Moo9^Yo..JMML.    .JMMmmmmMMM .JMML  JMML  JMML.`Moo9^Yo.`Ybmd9'  

  ''')


def search():
    GREEN(f'[+] Searching for username: {username}')
    time.sleep(0.5)
    print ('[                    ] 0% ')
    time.sleep(0.5)
    print ('[====================] 100%\n')
    time.sleep(0.5)

    GREEN(f'[+] † Eternal Demon † \n')
    time.sleep(0.5)
    print('==========================')
    time.sleep(0.5)
    print('==========================\n')
    time.sleep(0.5)

    time.sleep(1)

    count = 0
    match = True
    for url in WEBSITES:
        r = requests.get(url)

        if r.status_code == 200:
            if match == True:
                GREEN('[+] COINCIDENCIAS ENCONTRADOS')
                match = False
            YELLOW(f'\n{url} - {r.status_code} - OK')
            if username in r.text:
                GREEN(f'COINCIDENCIA POSITIVA: Nombre de usuario: {username}: se ha detectado texto en la URL')
            else:
                GREEN(f'COINCIDENCIA POSITIVA: Nombre de usuario: {username} - \033[91mtext NO se ha detectado en la URL, podría ser un FALSO POSITIVO')#
        count += 1

    total = len(WEBSITES)
    GREEN(f'FINALIZADO: Se encontraron un total de {count} coincidencias de {total} sitios web')

if __name__=='__main__':
    banner()
    search()

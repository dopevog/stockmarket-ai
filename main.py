import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("pandas-ta")
install("rich")

import smtplib
from subprocess import call
import os
import pandas as pd
import pandas_ta 
from pandas_datareader import data as pdr
from datetime import date
import datetime
import yfinance as yf
from colorama import Fore, init
init()
from rich import print as rprint
from time import sleep
yf.pdr_override()

exiting = Fore.RED + 'Exiting...'
e =[]
e = [] + [" "]
stock_list = pd.read_csv("SPX500.csv")
x = 1
number_of_stocks = 505
def listToString(e): 
    
    seprator = "\n- " 
    
    return (seprator.join(e))

sender = "oincstockmarketai@gmail.com"
password = "810-006501"

def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls')

clear()
i=0
while i < 1:
  exit = Fore.RED+"*Enter 'exit' at any point to exit"
  inpt = Fore.GREEN+'>> '
  opt = input(Fore.GREEN+f'''
  █▀ ▀█▀ █▀█ █▀▀ █▄▀ █▀▄▀█ ▄▀█ █▀█ █▄▀ █▀▀ ▀█▀   ▄▀█ █
  ▄█ ░█░ █▄█ █▄▄ █░█ █░▀░█ █▀█ █▀▄ █░█ ██▄ ░█░   █▀█ █

  Chose an option:
  a - about
  s - run the program
  c - credits
  {exit}
  {inpt}''')

  if opt == "a":
    print('''
  This program uses an algorithm which has been backtested and proven to give
  one hundred percent ROI. Yet, it is advisory to do your OWN research before investing.
  All stocks chosen beloing to the american American SPX index. If you decide to buy the
  stocks chosen by the program, then it is advisory to spend the same principle amount
  on each of them to minimise the risk.
    ''')
    rprint('''
  Check out the backtested result here: https://bit.ly/3bkh9QB
    ''')
    wait = input("")
    if wait == 'exit':
      clear()
      print(exiting)
      sleep(0.5)
      clear()
      break
    clear()

  elif opt == "c":
    print('''
  The program and algorithm are both developed by Vedant k. 
    ''')
    wait = input("")
    if wait == 'exit':
      clear()
      print(exiting)
      sleep(0.5)
      clear()
      break
    clear()

  elif opt == "s":
    email = input('''
  What is you email ID (The Stocks Chosen Will Be Sent To You Here): ''')
    if email == 'exit':
      clear()
      print(exiting)
      sleep(0.5)
      clear()
      break
    while x != number_of_stocks:
        ticker = stock_list.iloc[x]["Symbols"]
        today = date.today()
        start_date = today - datetime.timedelta(days = 365)
        data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
        openrate = data["Open"]
        close = data["Adj Close"]
        high = data["High"]
        low = data["Low"]
        data["RSI"] = pandas_ta.momentum.rsi(close, length=None, scalar=None, drift=None, offset=None)
        stoch = pandas_ta.momentum.stoch(high, low, close, k=None, d=None, smooth_k=None, offset=None)
        data["K"] = stoch.STOCHk_14_3_3
        data["D"] = stoch.STOCHd_14_3_3

        data['Up'] = data.RSI>60
        data['StochUp'] = (data.K>60) & (data.D>60) & (data.K<80) & (data.D<80)
        df = data.iloc[-3:]

        df.to_csv('df.csv')
        df = pd.read_csv('df.csv')

        cu = df.at[2,'Up']
        cy = df.at[1,'Up']
        cd = df.at[0,'Up']
        su = df.at[2,'StochUp']
        sy = df.at[1,'StochUp']
        sd = df.at[0,'StochUp']

        if cu == True & su == True:
            x = x+1
            if cy == False & cd == False:
                Buy = True
                e = e+[ticker]

        else:
            x = x+1

    clear()
    print(Fore.BLUE + "Sending Email...")
    out = listToString(e)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, password)
    message = f'''
    List Of Stocks With A Buy Signal: 
    {out}
    '''
    s.sendmail(sender, email, message)
    s.quit()
    print(Fore.BLUE + "Email Sent!")
    sleep(2)
    clear()
    break

  elif opt == "exit":
    clear()
    print(exiting)
    sleep(0.5)
    clear()
    break
  
  else:
    wait = input(Fore.RED+'''
  Please Enter A Valid Option''')
    if wait == 'exit':
      clear()
      print(exiting)
      sleep(0.5)
      clear()
      break
    clear()





    #df = pd.DataFrame()
    #help(df.ta)
    #df.ta.indicators()
    #help(pandas_ta.atr)

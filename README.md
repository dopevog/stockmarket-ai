# Short Term Stockmarket AI For American SPX Stocks
## Check It Out!
![t](https://user-images.githubusercontent.com/82938580/118754665-27a1ac00-b885-11eb-8ad6-954fa97d0fcb.gif)
## Run It Locally
You must add your email and password in ```main.py``` on line ```35``` & ```36```:
```
sender = "" ##Your Email
password = "" ## Your Email Password
```
Before doing so, you must activate [Less Secure Apps](https://myaccount.google.com/lesssecureapps) for your google account. 
```
git clone https://github.com/dopevog/stockmarket-ai.git
cd stockmarket-ai
pip3 install smtplib, pandas, pandas_ta, pandas_datareader, datetime, yfinance, colorama, rich
python3 main.py
```

## How Accurate Is It?
I __backtested__ it and it proved to have __100 % ROI__! Below is the backtested result:
![68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f7265706c69742f696d616765732f313632313330393930363634355f33353366653533356531376233343564363832663937323164646133376234632e706e67](https://user-images.githubusercontent.com/82938580/118754684-2e302380-b885-11eb-9598-bb78bd8b457a.png)


## License
This Project is [MIT Licensed](https://github.com/dopevog/stockmarket-ai/blob/main/LICENSE)

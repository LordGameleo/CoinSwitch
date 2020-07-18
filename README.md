# CoinSwitch
API for conversion rate from one currency to other

## Instruction to install and run server
Note: You need to have Python 3.6.1 or later, it is best to use python 3.7

- Install dependencies: pip install -r requirements.txt
- Run  Server: uvicorn main:app --reload

## Request format
To update currency database manually - 127.0.0.1:8000/set/
To get conversion rate - 127.0.0.1:8000/exchange/?final=ETH&initial=BTC 

## To use basic frontend
Go to 127.0.1:8000/docs

import time
from typing import Optional
import shrimpy
from fastapi import FastAPI

app = FastAPI()



# for i in range(0,len(curr)):
#     print(ticker[i]["name"] + " belongs to " + curr[ticker[i]["name"]]["name"])
curr = {}
time_last_update = time.perf_counter()
started = False
def run():
    global curr
    public_key = "6e66fa83ece4ca599e32339977647b5a211e0e401057cfd84b298c8dda40acab"
    private_key = "d416e67e3431d7ad706def03e6228f8dd90bb0d198ae76c7318cf189fab98cb6e51eb285609d1d2c65b79e5dcc2bfec5e97de05b80071391236d15abcee948e3"
    client = shrimpy.ShrimpyApiClient(public_key,private_key)
    ticker = client.get_ticker('kucoin')
    for i in range(0,len(ticker)):
        curr[ticker[i]["symbol"]] = ticker[i]

def conversion(initial, final):
    x = float(curr[initial]["priceBtc"])
    y = float(curr[final]["priceBtc"])
    return str(y/x)


@app.get("/set")
def update():
    global time_last_update
    run()
    time_last_update = time.perf_counter()
    return {'Update': 'Done', 'Number of Currencies': len(curr)}

@app.get("/exchange/")
def conversion_page(final:str = "", initial:str = ""):
    global time_last_update, started
    if time.perf_counter()-time_last_update>60 or started == False:
        run()
        time_last_update = time.perf_counter()
        started=True
        print("-------------Updated----------------")
    try:
        rate = {'Rate':conversion(initial,final)}
    except KeyError:
        rate = {'Error': 'Currency not found'}

    return rate

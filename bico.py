import requests
import json
try :
 prompt=int(input("enter data:"))
 b=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
 b=b.json()
 b=b["bpi"]["USD"]["rate"]
 b=float(b)
 q=b*prompt
 print(q)
except ValueError:
    print(f"your input is not an integer")

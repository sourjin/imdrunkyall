import requests
import sys
import json
if len(sys.argv )!= 2 :
    sys.exit("Missing command-line argument ")
else:
    a=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    try:
        float(sys.argv[1])
    except ValueError :
        sys.exit("Command-line argument is not a number")
a=a.json()
a=a["bpi"]["USD"]["rate_float"]
a=float(a)
b=float(sys.argv[1])*a
print(print(f"${b:,.4f}"))

import json
prom=input("enter a valid number: ")
if prom.isfloat :
    ("Missing command-line argument ")
else:
    a=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    try:
        float(prom)
    except ValueError :

a=a.json()
a=a["bpi"]["USD"]["rate_float"]
a=float(a)
b=float()*a
print(print(f"${b:,.4f}") )
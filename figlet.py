try:
 while True :
  from pyfiglet import Figlet
  import random
  import sys
  figlet = Figlet()
  fonts=figlet.getFonts()
  if len(sys.argv)== 0 :
    coin=figlet.choice(fonts)
    figlet.setFont(coin)
  elif sys.argv[1]== "-f" or sys.argv[1]== "--font" :
      if sys.argv[2] in fonts:
       figlet.setFont(font=sys.argv[2])
      else:
          sys.exit("Invalid usage")
  elif   sys.argv[1]!= "-f" or sys.argv[1]!= "--font" :
     sys.exit("Invalid usage")
  prompt=input("input: ")
  print(figlet.renderText(prompt))
  break

import inflect
s=[]
while True :
 try:
   pro=input("input:")
   p=inflect.engine()
   s.append(pro)
   sn=p.join(s)
 except EOFError :
   print("Adieu, adieu, to",sn)
   break

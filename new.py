prop=input("twttr name : ")
ler=[ 'a', 'e', 'i', 'o', 'u', 'A' ,'O', 'E', 'I','U' ]
for i in prop :
    if i in ler :
        prop=prop.replace(i," ")
        print(prop)
    else :
         print(prop)
         break

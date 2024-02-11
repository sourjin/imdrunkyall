n=int(input("soit Un>0 et n un entier naturel ; pour n="))
def fib(n) :
  if n< 2 :
    return (n)
  else :
   return (fib(n-2)+ fib(n-1))
print (fib(n))

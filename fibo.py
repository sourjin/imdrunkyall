def fib(n, memo={}):
    if n < 2:
        return n
    
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    
    return memo[n]

def main():
    n = int(input("Entrez un entier naturel n (n > 0): "))
    
    if n <= 0:
        print("Veuillez entrer un entier naturel supérieur à 0.")
    else:
        result = fib(n)
        print(f"Le terme Fibonacci pour n={n} est : {result}")

if __name__ == "__main__":
    main()

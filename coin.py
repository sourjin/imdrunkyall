import random

def main():
    int=get_level()
    generate_integer(int)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            continue


def generate_integer(level):
    trial = 0
    score =0
    for _ in range(10) :
      if level==1 :
             x=random.randint(0,9)
             y=random.randint(0,9)
      elif level== 2:
             x = random.randint(10, 99)
             y = random.randint(10, 99)
      else:
             x = random.randint(100,999)
             y = random.randint(100, 999)
      while True :
          print(f"{x} + {y} = " , end="")
          answer = input()
          if answer !=str(x+y) and trial!=2 :
             print("EEE")
             trial+=1
             continue
          elif answer ==str( x + y):
              score += 1
              break
          else:
             xx=x+y
             print(f"{x}+{y}={xx} ")
             break

    print("Score:" , score)

if __name__ == "__main__":
    main()

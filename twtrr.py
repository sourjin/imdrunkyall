def main() :
 user_input = input('type here: ')
 shorten(user_input)

def shorten(user_input) :
 ler=[ 'a', 'e', 'i', 'o', 'u', 'A' ,'O', 'E', 'I','U' ]
 for letter in user_input:
    if letter in ler :
        user_input = user_input.replace(letter, '')
 print(user_input)

main()
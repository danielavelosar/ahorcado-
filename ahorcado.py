import random
from typing import Dict
from os import system
def draw():
    print(r"""\

                            .-----.
                    \ ' /   _/    )/
                    - ( ) -('---''--)
                    / . \((()\^_^/)()
                    \\_\ (()_)-((()()
                    '- \ )/\._./(()
                        '/\/( X   ) \
                        (___)|___/ ) \
                            |.#_|(___)
                            /\    \ ( (_
                            \/\/\/\) \\
                            | / \ |
                            |(   \|
                            _|_)__|_\_
                            )...()...(
                            | (   \ |     
                        .-'__,)  (  \
                    mrf           '\_-,

                """)
def get_word():
    with open("./archivos/data.txt","r",encoding=('utf-8')) as f:
        words = []
        for word in f:
            words.append(word) 
        position = random.randint(0, (len(words)-1))
        return words[position]
def print_word(word, dict_word, dict_new_word, position):
    printing = ["_ " for i in range (len(word)-1)]
    print(printing)
    letter_guessed = dict_word.get(position)
    print(letter_guessed)

def verify_word(word, dict_word, dict_new_word = {}):
    print_word(word, dict_word, dict_new_word, position = None)
    letter_chosen = input("ingresa la letra = ")
    if map(lambda letter : letter != letter_chosen , word):
        new_word = list(filter(lambda letter : letter != letter_chosen , word))
        positions = list(map(lambda letter : letter != letter_chosen , word))
        for position in positions:
            if position == False :
                print_word(word, dict_word, dict_new_word,position)
        print(positions)
    print("prueba otra vez")
    return[new_word]    
    

    
def screen():
    print('bienvenido a ahorcado!')
    word = get_word()
    word_dict ={letter for letter in sorted(enumerate(word))}
    print(word_dict)
    verify_word(word, word_dict)
    print('adivina la letra')
    #draw()


def main():
    screen()

if __name__=="__main__":
    main()
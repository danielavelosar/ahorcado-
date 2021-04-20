import random
from typing import Dict, Match
from os import replace, system
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
            word.replace('\n','')
            words.append(word) 
        position = random.randint(0, (len(words)-1))
        return words[position]
def letters_choice(word, lines):
    while word != lines :
        letter_chosen = input("ingresa la letra = ")
        i = 0
        for letter in word:
            if letter_chosen == letter:
                lines[i] = letter_chosen    
            i += 1
        print(''.join(lines))
        if letter_chosen not in word:
            print('inténtalo otra vez')    
        
    print('ganaste!')    
        
           




                
   
    
    
    
    
def screen():
    print('bienvenido a ahorcado!')
    word = list(get_word())
    word.pop(len(word)-1)
    print(word)
    #word_dict ={letter for letter in sorted(enumerate(word))}
    #print(word_dict)
    lines = ['_']*len(word)
    print(lines[0:2])
    print(''.join(lines))
    letters_choice(word, lines)
    print('adivina la letra')
    #draw()


def main():
    screen()

if __name__=="__main__":
    main()
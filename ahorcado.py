import random
from typing import Dict, Match
import os
from unicodedata import normalize
import re

def draw(strikes):
    if strikes == 1:
        print(r"""\

                                .-----.
                        \ ' /   _/    )/
                        - ( ) -('---''--)


                    """)
    if strikes == 2:
        print(r"""\

                                .-----.
                        \ ' /   _/    )/
                        - ( ) -('---''--)
                        / . \((()\^_^/)()
                        \\_\ (()_)-((()()
                        '- \ )/\._./(()
                           

                    """)
    if strikes == 3:
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
                                
                    """)
    if strikes == 4:
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
                    """)
    if strikes == 5:
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

                    perdiste :)
                    """)
    if strikes == 6:
        os.system('cls')
        print('escribe ctrl l para salir del juego')
        
def get_word():
    with open("./archivos/data.txt","r",encoding=('utf-8')) as f:
        words = []
        for word in f:
            word.replace('\n','')
            words.append(word) 
        position = random.randint(0, (len(words)-1))
        return words[position]
def letters_choice(word, lines, strikes):
    letter_chosen = input("ingresa la letra = ")
    letter_chosen = letter_chosen.strip()
    
    i = 0
    
    for letter in word:
        if letter_chosen == letter:
            lines[i] = letter_chosen
        os.system('cls')    
        i += 1
    if letter_chosen not in word:
        print('inténtalo otra vez')
        strikes +=1
    assert len(letter_chosen) < 2, 'escribe una letra por favor' 
    assert isinstance(letter_chosen, str), 'escoge una letra por favor'
    
    return(lines, strikes)    

def accent_solver(word):
    # -> NFD y eliminar diacríticos
    word = re.sub(
            r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
            normalize( "NFD", word), 0, re.I
        )

    # -> NFC
    word = normalize( 'NFC', word)
    word = word.lower()
    word = list(word)
    word.pop(len(word)-1)
    return word
        
           
def screen():
    strikes = 0
    print('bienvenido a ahorcado!')
    print('adivina la letra')
    word = get_word()
    word = accent_solver(word)
    #word_dict ={letter for letter in sorted(enumerate(word))}
    #print(word_dict)
    lines = ['_']*len(word)
    print(''.join(lines))
    while word != lines and strikes <=5 :
        lines, strikes = letters_choice(word, lines, strikes)
        draw(strikes)
        print(''.join(lines))    
    print('ganaste!') 
    
    #draw()




def main():
    screen()

if __name__=="__main__":
    main()
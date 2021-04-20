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
def letters_choice(word, letters_chosen = []):
    new_word = word
    while len(new_word) >= 0:
        print(word)
        letter_chosen = input("ingresa la letra = ")
        letters_chosen.append(letter_chosen)
        print(f'letters= {letters_chosen}')
        letter_match = list(map(lambda letter : letter == letter_chosen, word))
        new_word = list((filter(lambda letter : letter == letter_chosen, word)))
        verify_word(new_word, letter_match, letters_chosen)
        
           




def verify_word(word, letter_match, letters_chosen):
    word_dict = dict(filter(lambda letter : letter, enumerate(word)))
    positions=[]
    for letter_chosen in letters_chosen:
        for keys, values in word_dict.items():
            if letter_chosen == values:
                positions.append(keys) 
        printing = [] 
        
    for letter in letter_match:
        if letter:
            for position in positions:
                printing.append(word_dict.get(position))
                positions.remove(position)
        printing.append("_")
        
    print(" ".join(printing))
    
    
    
    
def screen():
    print('bienvenido a ahorcado!')
    word = get_word()
    #word_dict ={letter for letter in sorted(enumerate(word))}
    #print(word_dict)
    letters_choice(word)
    print('adivina la letra')
    #draw()


def main():
    screen()

if __name__=="__main__":
    main()
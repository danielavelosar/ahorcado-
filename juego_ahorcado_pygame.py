import pygame, sys
from pygame.locals import *
import random
 
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
 
# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (235, 226, 225)
LIGHT_GRAY = (181, 176, 176)
DARK_GRAY = (105, 102, 101)
PINK = (236, 170, 158)
BROWN = (105, 75, 70)
FONT = pygame.font.Font(None, 32)
 
# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((300,300))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Ahorcado")

def get_word():
    with open("./archivos/data.txt","r",encoding=('utf-8')) as f:
        words = []
        for word in f:
            word.replace('\n','')
            words.append(word) 
        position = random.randint(0, (len(words)-1))
        return(words[position]) 
   
# Creating Lines and Shapes
class Hangman(pygame.sprite.Sprite):
    def __init__(self):
        super.__init__
        self.image = pygame.image.load("img/ionic-3-ahorcado.png")
        self.word = list(get_word())
    def print(self):
        self.word.pop(len(self.word)-1)
        lines = ['_']*len(self.word)
        while self.word != lines :
            letter_chosen = input("ingresa la letra = ")
            i = 0
            for letter in self.word:
                if letter_chosen == letter:
                    lines[i] = letter_chosen    
                i += 1
            print(''.join(lines))
            if letter_chosen not in self.word:
                print('inténtalo otra vez')    
        
        print('ganaste!') 
class NameBox(pygame.sprite.Sprite):#subclase más simple para hacer objetos en python
    def __init__(self, x, y, z, w, letter = ''):
        self.rect = pygame.Rect(x, y, z, w)
        self.color = LIGHT_GRAY
        self.text = letter
        self.font = FONT.render(self.text, True, self.color)
        self.active = False
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: # mira las cosas con el mouse 
            if pygame.Rect.collidepoint(event.pos): #verifica si se da click 
                self.active = not self.active # buena manera de ambiar el booleano :)
            else: self.active = False  
            self.color = DARK_GRAY if self.active else LIGHT_GRAY #cambiar el color de la caja
        if event.type == pygame.KEYDOWN: #si maneja el teclado (permite hacer strings)
            if event.key == K_RETURN: # si  lo que tecleas es igual a lo que retorna ?
                print(self.text)
                self.text = ''
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1] # takes everything except the last item 
            else: 
                self.text += event.unicode #agrega el texto string
            self.font = FONT.render(self.text, True, self.color)# re-render text
    def draw(self, screen):
        # blit esdibujar algo en pantalla 
        screen.blit(self.font, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

    
HM = Hangman()
# Beginning Game Loop
while True:
    input_box1 = NameBox(100, 100, 140, 32)
    input_box2 = NameBox(100, 300, 140, 32)
    input_boxes = [input_box1, input_box2]
    done = False

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            #sys.exit()
        for box in input_boxes:
            box.handle_event(event)
    DISPLAYSURF.fill((30, 30, 30))
    for box in input_boxes:
        box.draw(DISPLAYSURF)

    pygame.display.flip()
    FramePerSec.tick(FPS)
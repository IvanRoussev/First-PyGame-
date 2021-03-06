from cgitb import grey
import itertools
from turtle import back
from venv import create
import pygame
import random
import pygame.locals
import random

x = 100
y = 95
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (127, 127, 127)

class Bob(pygame.sprite.Sprite):
    """ This is the main player Class """
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load('./week12Lab/bob.jpg')
        self.image = pygame.transform.scale(self.original_image, (x, y))
        self.rect = self.image.get_rect()

        self.rect.x = 200
        self.rect.y = 200

def create_text_surface(text):
    """This function creates a surface and renders the text argument in it"""
    arial = pygame.font.SysFont('arial', 24)
    text_surface = arial.render(text, True, (0, 0, 0))

    return text_surface

start_ticks=pygame.time.get_ticks() #starter tick






def main():
    """ Main function to run the game """
    pygame.init()

    # Screen is 500x500 pixels
    window = pygame.display.set_mode((500, 500))
    clock = pygame.time.clock()
    start = pygame.time.get_ticks()
    # New player
    bob = Bob()
    

    running = True

    score = 0
    misses = 0
    window.fill(GRAY)

    while running:        

        
        

        # Event loop - quit if closed or 'escape' is pressed
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                running = False
            elif event.type == pygame.locals.KEYDOWN:
                if event.key in (pygame.locals.K_ESCAPE, pygame.locals.K_q):
                    running = False
            elif event.type == pygame.locals.MOUSEBUTTONDOWN:
                mouse = event.pos
                if bob.rect.collidepoint(mouse):
                    window.fill(GREEN)
                    pygame.display.update()
                    bob.rect.x = random.randint(10,400)
                    bob.rect.y = random.randint(10,400)
                    window.blit(bob.image, bob.rect)
                    score += 1
                    print(f'Your Current Score = {score}')
                    
                else:
                    window.fill(RED)
                    pygame.display.update()
                    misses += 1
                    print(f'Misses = {misses}')


            elif score == 10:
                window.fill(GRAY)
                surf = create_text_surface('FInal Score: ' + str(score))
                window.blit(surf, (200, 250))
                pygame.display.update()
                pygame.time.wait(5000)
                print(f'-----Final Score is {score}-----\n-----You Missed {misses} times-----')
                break
        
        text_score = f'Score: {score}'

        text_surface = create_text_surface(text_score)       
        window.blit(text_surface, (0, 0))
        window.blit(bob.image, bob.rect)
        # Update the screen
        pygame.display.update()
        


if __name__ == "__main__":
    main()
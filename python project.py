#*************************************************

# Author: Catharine and Noshin

# Date: December 11, 2021

# Last modified: December 18, 2021 9:04 pm by Catharine

# Name: Python Project (Wildlife Survival Guide)

# Description: Pygame project which teaches a lesson about wildlife survival

#*************************************************

# Import modules
import pygame
pygame.init() # Initialize pygame
import platform
import os, time
from pygame import mixer
from pygame.locals import *

# Declare and initialize variables
gameExit = bool()
clock = pygame.time.Clock()
homeScreenBg = pygame.image.load('images/WildlifeSurvivalBg.png')
animationBg = pygame.image.load('images/animationscenariobg.png')
animation1Bg = pygame.image.load('images/animation1bg.png')
animation2s1Bg = pygame.image.load('images/animation2s1.png')
lesson1Bg = pygame.image.load('images/lesson1.png')
lesson2Bg = pygame.image.load('images/lesson2.png')
icon = pygame.image.load('images/icon.png')
storyButton = pygame.image.load('images/interactivestorybutton.png')
storyButton = pygame.transform.scale(storyButton, (227, 71))
instructionsButton = pygame.image.load('images/instructionsbutton.png')
instructionsButton = pygame.transform.scale(instructionsButton, (227, 71))
lessonButton = pygame.image.load('images/lessonbutton.png')
lessonButton = pygame.transform.scale(lessonButton, (227, 71))
quizButton = pygame.image.load('images/quizbutton.png')
quizButton = pygame.transform.scale(quizButton, (227, 71))
quizResultsButton = pygame.image.load('images/quizresultsbutton.png')
quizResultsButton = pygame.transform.scale(quizResultsButton, (227, 71))
exitButton = pygame.image.load('images/exitbutton.png')
exitButton = pygame.transform.scale(exitButton, (227, 71))

# Necessary for python to work on tdsb computers
if platform.system() == 'Windows':
    os.environ['SDL_VIDEODRIVER'] = 'windib'

# Define functions
def gameLoop():
    gameExit = False
    show = 'Main Menu'
    
    gameDisplay = pygame.display.set_mode((800, 600)) # Sets display size
    pygame.display.set_caption('Wildlife Survival Guide') # Sets caption at top to Wildlife Survival Guide
    pygame.display.set_icon(icon) # Sets icon   
    
    pygame.display.update()
    
    gameDisplay.fill((0, 0, 0)) # Set background as black 
    gameDisplay.blit(homeScreenBg, (0, 0)) # Sets background image
    
    # Load buttons
    gameDisplay.blit(storyButton, (43, 264))
    gameDisplay.blit(instructionsButton, (286, 264))
    gameDisplay.blit(lessonButton, (529, 264))
    gameDisplay.blit(quizButton, (43, 378))
    gameDisplay.blit(quizResultsButton, (286, 378))
    gameDisplay.blit(exitButton, (529, 378))        
    
    # Background music
    mixer.music.load('music/DynamiteInstrumental.mp3')
    mixer.music.play(-1) # -1 is to keep the music looping         
        
    pygame.display.update()
    
    clock.tick(60)      
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            clicked = pygame.mouse.get_pressed()
            x = clickPos[0]
            y = clickPos[1]
            
            # Checks if where the user clicked is in the range of a button
            if show == 'Main Menu':
                if x >= 43 and x <= 271:
                    if y >= 264 and y <= 336:
                        if clicked[0] == 1:
                            show = 'Animation'
                            animation()
                    elif y >= 378 and y <= 449:
                        if clicked[0] == 1:
                            show = 'Quiz'                
                elif x >= 286 and x <= 513:
                    if y >= 264 and y <= 336:
                        if clicked[0] == 1:
                            show = 'Instructions'
                    elif y >= 378 and y <= 449:
                        if clicked[0] == 1:
                            show = 'Quiz Results'                             
                elif x >= 529 and x <= 756:
                    if y >= 264 and y <= 336:
                        if clicked[0] == 1:
                            show = 'Lesson' 
                            lesson()
                    elif y >= 378 and y <= 449:
                        if clicked[0] == 1:
                            pygame.quit() 
                            quit()
        
            # Exits the game
            if event == pygame.quit:
                pygame.quit()
                quit()
                
def animation():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animationBg, (0, 0)) # Sets background image
    pygame.display.update()   
    clock.tick(60)
    show = 'Animation'
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            clicked = pygame.mouse.get_pressed()
            x = clickPos[0]
            y = clickPos[1] 
            
            if show == 'Animation':
                if y >= 505 and y <= 575:
                    if x >= 547 and x <= 773:
                        if clicked[0] == 1:
                            show = "Animation1"
                            animation1()
                        
def animation1():
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animation1Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)   
    show = 'Animation1'
                
def lesson():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(lesson1Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    show = 'Lesson'
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            clicked = pygame.mouse.get_pressed()
            x = clickPos[0]
            y = clickPos[1]    
            
            if show == 'Lesson':
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        if clicked[0] == 1:
                            show = 'Main Menu' 
                            gameLoop()
                    elif x >= 524 and x <= 751:
                        if clicked[0] == 1:
                            show = 'Lesson2'
                            lesson2()
                            
def lesson2():
    gameExit = False 
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(lesson2Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    show = 'Lesson2'   
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            clicked = pygame.mouse.get_pressed()
            x = clickPos[0]
            y = clickPos[1]
            
            if show == 'Lesson2':
                if y >= 477 and y <= 548:
                    if x >= 524 and x <= 751:
                        if clicked[0] == 1:
                            show = 'Lesson'
                            lesson()
                    elif x >= 48 and x <= 276:
                        if clicked[0] == 1:
                            show = 'Main Menu'
                            gameLoop()

# Main program
# Start game loop
gameLoop()

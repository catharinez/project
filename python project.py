#*************************************************

# Author: Catharine and Noshin

# Date: December 11, 2021

# Last modified: December 14, 2021 9:33 pm by Catharine

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
displayWidth = int(800)
displayHeight = int(600)
gameExit = bool()
clock = pygame.time.Clock()
homeScreenBg = pygame.image.load('images/WildlifeSurvivalBg.png')
animationBg = pygame.image.load('images/animationscenariobg.png')
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
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

# Define functions
def gameLoop():
    gameExit = False
    show = "Welcome"
    print("loop")
    
    gameDisplay = pygame.display.set_mode((displayWidth, displayHeight)) # Sets display size
    pygame.display.set_caption('Wildlife Survival Guide') # Sets caption at top to Wildlife Survival Guide
    pygame.display.set_icon(icon) # Sets icon   
    
    pygame.display.update()
    
    if show == "Welcome":
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
    
    elif show == "Animation":
        gameDisplay.fill((0, 0, 0)) # Set background as black 
        gameDisplay.blit(animationBg, (0, 0)) # Sets background image
                              
        pygame.display.update()   
        
        clock.tick(60)
        
    elif show == "Instructions":
        gameDisplay.fill((0, 0, 0)) # Set background as black 
    
        pygame.display.update()   
    
        clock.tick(60)        

    elif show == "Lesson":
        gameDisplay.fill((0, 0, 0)) # Set background as black 
    
        pygame.display.update()   
    
        clock.tick(60)        
    
    elif show == "Quiz":
        gameDisplay.fill((0, 0, 0)) # Set background as black 
    
        pygame.display.update()   
    
        clock.tick(60)   
    elif show == "Quiz Results":
        gameDisplay.fill((0, 0, 0)) # Set background as black 
    
        pygame.display.update()   
    
        clock.tick(60)         
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            clicked = pygame.mouse.get_pressed()
            x = clickPos[0]
            y = clickPos[1]
        
            print(x, y, clicked)
            
            # Checks if where the user clicked is in the range of a button
            if show == "Welcome":
                if x >= 43 and x <= 271:
                    if y >= 264 and y <= 336:
                        if clicked[0] == 1:
                            gameDisplay.fill((0, 0, 0))
                            gameDisplay.blit(animationBg, (0, 0)) # Sets background image
                            pygame.display.update()
                            show = "Animation"
                            break
                    elif y >= 378 and y <= 449:
                        if clicked[0] == 1:
                            show = "Quiz" # This button changes show from 'Welcome' to 'Quiz'                    
                elif x >= 286 and x <= 513:
                    if y >= 264 and y <= 336:
                        if clicked[0] == 1:
                            show = "Instructions" # This button changes show from 'Welcome' to 'Instructions'
                    elif y >= 378 and y <= 449:
                        if clicked[0] == 1:
                            show = "Quiz Results" # This button changes show from 'Welcome' to 'Quiz Results'                            
                elif x >= 529 and x <= 756:
                    if y >= 264 and y <= 336:
                        if clicked[0] == 1:
                            show = "Lesson" # This button changes show from 'Welcome' to 'Lesson'   
                    elif y >= 378 and y <= 449:
                        if clicked[0] == 1:
                            pygame.quit() # This button allows the user the exit the program
                            quit()
        
            # Exits the game
            if event == pygame.quit:
                pygame.quit()
                quit()                
            
# Main program
# Start game loop
gameLoop()
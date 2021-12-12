#*************************************************

# Author: Catharine and Noshin

# Date: December 11, 2021

# Last modified: December 11, 2021 11:05 am by Catharine

# Name: Python Project (Wildlife Survival Guide)

# Description: Pygame project which teaches a lesson about wildlife survival

#*************************************************

# Import modules
import pygame
pygame.init() # Initialize pygame
import platform
import os, time
from pygame import mixer

# Necessary for python to work on tdsb computers
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

# Define functions
def gameLoop():
    gameExit = False
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                quit()
         
        gameDisplay.fill((0, 0, 0)) # Set background as black 
        gameDisplay.blit(homeScreenBg, (0, 0)) # Sets background image
        
        # Load buttons
        gameDisplay.blit(storyButton, (43, 264))
        gameDisplay.blit(instructionsButton, (286, 264))
        gameDisplay.blit(lessonButton, (529, 264))
        gameDisplay.blit(quizButton, (43, 378))
        gameDisplay.blit(quizResultsButton, (286, 378))
        gameDisplay.blit(exitButton, (529, 378))
            
        pygame.display.update()
        
        clock.tick(60)
            
# Main program
# Declare and initialize variables
displayWidth = int(800)
displayHeight = int(600)
gameExit = bool()
homeScreenBg = pygame.image.load('images/WildlifeSurvivalBg.png')
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

# Display screen
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Wildlife Survival Guide') # Sets caption at top to Wildlife Survival Guide
pygame.display.set_icon(icon) # Sets icon

# Background image and music
mixer.music.load('music/DynamiteInstrumental.mp3')
mixer.music.play(-1) # -1 is to keep the music looping 

clock = pygame.time.Clock()

gameLoop() # Start the game loop


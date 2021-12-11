#*************************************************

# Author: Catharine and Noshin

# Date: December 11, 2021

# Last modified: December 11, 2021 4:18 pm by Catharine

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
    x = 0
    y = 0
    gameExit = False
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                quit()
         
        gameDisplay.fill((0, 0, 0)) #set background as green 
        homeScreen(x, y)
            
        pygame.display.update()
        
        clock.tick(60)
        
def homeScreen(x, y):        
    gameDisplay.blit(homeScreenBg, (x, y))
            
# Main program
# Declare and initialize variables
displayWidth = int(800)
displayHeight = int(600)
gameExit = bool()
homeScreenBg = pygame.image.load('WildlifeSurvivalHomeScreen.png')
icon = pygame.image.load('icon.png')

# Display screen
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Wildlife Survival Guide') # Sets caption at top to Wildlife Survival Guide
pygame.display.set_icon(icon) # Sets icon

# Background music
mixer.music.load('DynamiteInstrumental.mp3')
mixer.music.play(-1) # -1 is to keep the music looping 

clock = pygame.time.Clock()

gameLoop()

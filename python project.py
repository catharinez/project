#*************************************************

# Author: Catharine and Noshin

# Date: December 11, 2021

# Last modified: January 3, 2022 5:32 pm by Catharine

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
clock = pygame.time.Clock()
homeScreenBg = pygame.image.load('images/WildlifeSurvivalBg.png')
animationBg = pygame.image.load('images/animationscenariobg.png')
animation1Bg = pygame.image.load('images/animation1bg.png')
animation2s1Bg = pygame.image.load('images/animation2s1.png')
animation2s2Bg = pygame.image.load('images/animation2s2.png')
animation21Bg = pygame.image.load('images/animation21.png')
animation3Bg = pygame.image.load('images/animation3.png')
animation4Bg = pygame.image.load('images/animation4.png')
animation5Bg = pygame.image.load('images/animation5.png')
animationEnding1Bg = pygame.image.load('images/animationending1.png')
animationEnding2Bg = pygame.image.load('images/animationending2.png')
animationEnding3Bg = pygame.image.load('images/animationending3.png')
animationEnding4Bg = pygame.image.load('images/animationending4.png')
animationEnding5Bg = pygame.image.load('images/animationending5.png')
instructionsBg = pygame.image.load('images/instructions.png')
lesson1Bg = pygame.image.load('images/lesson1.png')
lesson2Bg = pygame.image.load('images/lesson2.png')
citations1Bg = pygame.image.load('images/citations1.png')
citations2Bg = pygame.image.load('images/citations2.png')
citations3Bg = pygame.image.load('images/citations3.png')
citations4Bg = pygame.image.load('images/citations4.png')
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

# Function which keeps the program running
def gameLoop():
    gameExit = False
    
    gameDisplay = pygame.display.set_mode((800, 600)) # Sets display size
    pygame.display.set_caption('Wildlife Survival Guide') # Sets caption at top to Wildlife Survival Guide
    pygame.display.set_icon(icon) # Sets icon   
    
    pygame.display.update()
    
    # Sets background
    gameDisplay.fill((0, 0, 0)) 
    gameDisplay.blit(homeScreenBg, (0, 0)) 
    
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
    
    # While loop used for the buttons
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Checks if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if x >= 43 and x <= 271:
                    if y >= 264 and y <= 336:
                        animation()
                    elif y >= 378 and y <= 449:
                        print() # This will be left here until we finish the quiz results to prevent an error due to indentation
                        # quiz() This is for once we finish the quiz
                elif x >= 286 and x <= 513:
                    if y >= 264 and y <= 336:
                        instructions()
                    elif y >= 378 and y <= 449:
                        print() # This will be left here until we finish the quiz results to prevent an error due to indentation
                        # quizresults() This is for once we finish the quiz results                            
                elif x >= 529 and x <= 756:
                    if y >= 264 and y <= 336:
                        lesson()
                    elif y >= 378 and y <= 449:
                        pygame.quit() 
                        quit()
        
            # Exits the game
            if event == pygame.quit:
                pygame.quit()
                quit()

# Function for the animation                
def animation():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animationBg, (0, 0)) # Sets background image
    pygame.display.update()   
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1] 
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 505 and y <= 575:
                    if x >= 547 and x <= 773:
                        animation1()

# Function for Part 1 of the animation                        
def animation1():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animation1Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)   
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        animation2s1()
                    elif x >= 513 and x <= 740:
                        animation2s2()

# Function for part 2 scenario 1 of the animation                            
def animation2s1():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animation2s1Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        animation3()
                    elif x >= 513 and x <= 740:
                        ending1()                

# Function for part 2 scenario 2 of the animation    
def animation2s2():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animation2s2Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]   
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        ending2()
                    elif x >= 513 and x <= 740:  
                        animation21()
                            
# Function for part 2.1 of the animation
def animation21():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animation21Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        animation3()
                    elif x >= 513 and x <= 740:
                        ending1()      
    
# Function for part 3 of the animation
def animation3():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animation3Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)   
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        ending3() 
                    elif x >= 513 and x <= 740:
                        animation4()                            

# Function for part 4 of the animation                            
def animation4():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animation4Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        ending4()
                    elif x >= 513 and x <= 740:
                        animation5()                            
                            
# Function for part 5 of the animation
def animation5():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animation5Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)     
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 513 and x <= 740:
                        ending5()    
    

# Function for ending 1 of the animation
def ending1():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animationEnding1Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)  
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        gameLoop()
                    elif x >= 513 and x <= 740:
                        pygame.quit()
                        quit()    

# Function for ending 2 of the animation                            
def ending2():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animationEnding2Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)   
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        gameLoop()
                    elif x >= 513 and x <= 740:
                        pygame.quit()
                        quit()

# Function for ending 3 of the animation                            
def ending3():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animationEnding3Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        gameLoop()
                    elif x >= 513 and x <= 740:
                        pygame.quit()
                        quit()

# Function for ending 4 of the animation                            
def ending4():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animationEnding4Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        gameLoop()
                    elif x >= 513 and x <= 740:
                        pygame.quit()
                        quit()        

# Function for ending 5 of the animation                            
def ending5():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animationEnding5Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)    
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        gameLoop()
                    elif x >= 513 and x <= 740:
                        pygame.quit()
                        quit()    
                            
# Function for the instructions
def instructions():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(instructionsBg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)  
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]    
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        gameLoop()    

# Function for the lesson                
def lesson():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(lesson1Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]    
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        gameLoop()
                    elif x >= 524 and x <= 751:
                        lesson2()

# Function for the second part of the lesson                            
def lesson2():
    gameExit = False 
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(lesson2Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60) 
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        lesson()
                    elif x >= 524 and x <= 751:
                        citations1()

# Function for the first part of the citations                            
def citations1():
    gameExit = False 
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(citations1Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        lesson2()
                    elif x >= 524 and x <= 751:
                        citations2()    

# Function for the second part of the citations                            
def citations2():
    gameExit = False 
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(citations2Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        citations1()
                    elif x >= 524 and x <= 751:
                        citations3()  

# Function for the third part of the citations
def citations3():
    gameExit = False 
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(citations3Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        citations2()
                    elif x >= 524 and x <= 751:
                        citations4()  

# Function for the fourth part of the citations                            
def citations4():
    gameExit = False 
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(citations4Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        citations3()

# Start game loop
gameLoop()
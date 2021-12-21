#*************************************************

# Author: Catharine and Noshin

# Date: December 11, 2021

# Last modified: December 21, 2021 11:27 am by Catharine

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

# Function which keeps the program running
def gameLoop():
    gameExit = False
    show = 'Main Menu'
    
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
            if show == 'Main Menu':
                if x >= 43 and x <= 271:
                    if y >= 264 and y <= 336:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Animation'
                            animation()
                    elif y >= 378 and y <= 449:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Quiz'                
                elif x >= 286 and x <= 513:
                    if y >= 264 and y <= 336:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Instructions'
                    elif y >= 378 and y <= 449:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Quiz Results'                             
                elif x >= 529 and x <= 756:
                    if y >= 264 and y <= 336:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Lesson' 
                            lesson()
                    elif y >= 378 and y <= 449:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
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
    show = 'Animation'
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1] 
            
            if show == 'Animation':
                if y >= 505 and y <= 575:
                    if x >= 547 and x <= 773:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Animation1'
                            animation1()

# Function for Part 1 of the animation                        
def animation1():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animation1Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)   
    show = 'Animation1'
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if show == 'Animation1':
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Animation2s1'
                            animation2s1()
                    elif x >= 513 and x <= 740:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Animation2s2'
                            animation2s2()

# Function for part 2 scenario 1 of the animation                            
def animation2s1():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animation2s1Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    show = 'Animation2s1'
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if show == 'Animation2s1':
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Animation3'
                            animation3()
                    elif x >= 513 and x <= 740:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'AnimationEnding1'
                            ending1()                

# Function for part 2 scenario 2 of the animation    
def animation2s2():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animation2s2Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    show = 'Animation2s2' 
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]   
            
            if show == 'Animation2s2':
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'AnimationEnding2'
                            ending2()
                    elif x >= 513 and x <= 740:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Animation2.1'   
                            animation21()
                            
# Function for part 2.1 of the animation
def animation21():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animation21Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    show = 'Animation2.1'
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if show == 'Animation2.1':
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Animation3'
                            animation3()
                    elif x >= 513 and x <= 740:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'AnimationEnding1'
                            ending1()      
    
# Function for part 3 of the animation
def animation3():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animation3Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    show = 'Animation3'    
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if show == 'Animation3':
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'AnimationEnding3'
                            ending3() 
                    elif x >= 513 and x <= 740:
                        if ev.type == pygame.MOUSEBUTTONDOWN:  
                            show = 'Animation4'
                            animation4()                            

# Function for part 4 of the animation                            
def animation4():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animation4Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    show = 'Animation4' 
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if show == 'Animation4':
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'AnimationEnding4'    
                            ending4()
                    elif x >= 513 and x <= 740:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Animation5'
                            animation5()                            
                            
# Function for part 5 of the animation
def animation5():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animation5Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    show = 'Animation5'     
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if show == 'Animation5':
                if y >= 483 and y <= 554:
                    if x >= 513 and x <= 740:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'AnimationEnding5'
                            ending5()    
    

# Function for ending 1 of the animation
def ending1():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animationEnding1Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    show = 'AnimationEnding1'   
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if show == 'AnimationEnding1':
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Main Menu'
                            gameLoop()
                    elif x >= 513 and x <= 740:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
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
    show = 'AnimationEnding2'    
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if show == 'AnimationEnding2':
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Main Menu'
                            gameLoop()
                    elif x >= 513 and x <= 740:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            pygame.quit()
                            quit()
                            
def ending3():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animationEnding3Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    show = 'AnimationEnding3'    
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if show == 'AnimationEnding3':
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Main Menu'
                            gameLoop()
                    elif x >= 513 and x <= 740:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            pygame.quit()
                            quit()
                            
def ending4():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animationEnding4Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    show = 'AnimationEnding4'
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if show == 'AnimationEnding4':
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Main Menu'
                            gameLoop()
                    elif x >= 513 and x <= 740:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            pygame.quit()
                            quit()        
                            
def ending5():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.fill((0, 0, 0))
    gameDisplay.blit(animationEnding5Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)
    show = 'AnimationEnding5'    
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            if show == 'AnimationEnding5':
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Main Menu'
                            gameLoop()
                    elif x >= 513 and x <= 740:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            pygame.quit()
                            quit()    

# Function for the lesson                
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
            x = clickPos[0]
            y = clickPos[1]    
            
            if show == 'Lesson':
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Main Menu' 
                            gameLoop()
                    elif x >= 524 and x <= 751:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Lesson2'
                            lesson2()

# Function for the second part of the lesson                            
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
            x = clickPos[0]
            y = clickPos[1]
            
            if show == 'Lesson2':
                if y >= 477 and y <= 548:
                    if x >= 524 and x <= 751:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Lesson'
                            lesson()
                    elif x >= 48 and x <= 276:
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            show = 'Main Menu'
                            gameLoop()

# Start game loop
gameLoop()
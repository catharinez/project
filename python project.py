#*************************************************

# Author: Catharine and Noshin

# Date: December 11, 2021

# Last modified: January 17, 2022 10:08 am by Catharine and Noshin

# Name: Python Project (Wildlife Survival Guide)

# Description: Pygame project which teaches a lesson about wildlife survival

#*************************************************

# Import modules
import pygame
pygame.init() # Initialize pygame
pygame.display.init()
import platform
import os, time
from pygame import mixer
from pygame.locals import *

# Declare and initialize variables
clock = pygame.time.Clock()
numberOfCorrect = int(0)
titleScreenBg = pygame.image.load('images/titlescreenbg.png')
mainMenuBg = pygame.image.load('images/WildlifeSurvivalBg.png')
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
quizInstructionsBg = pygame.image.load('images/quizinstructions.png')
quizQuestion1Bg = pygame.image.load('images/quizq1.png')
quizQuestion2Bg = pygame.image.load('images/quizq2.png')
quizQuestion3Bg = pygame.image.load('images/quizq3.png')
quizQuestion4Bg = pygame.image.load('images/quizq4.png')
quizQuestion5Bg = pygame.image.load('images/quizq5.png')
quizQuestion1CorrectBg = pygame.image.load('images/quizq1correct.png')
quizQuestion2CorrectBg = pygame.image.load('images/quizq2correct.png')
quizQuestion3CorrectBg = pygame.image.load('images/quizq3correct.png')
quizQuestion4CorrectBg = pygame.image.load('images/quizq4correct.png')
quizQuestion5CorrectBg = pygame.image.load('images/quizq5correct.png')
quizQuestion1IncorrectBg = pygame.image.load('images/quizq1incorrect.png')
quizQuestion2IncorrectBg = pygame.image.load('images/quizq2incorrect.png')
quizQuestion3IncorrectBg = pygame.image.load('images/quizq3incorrect.png')
quizQuestion4IncorrectBg = pygame.image.load('images/quizq4incorrect.png')
quizQuestion5IncorrectBg = pygame.image.load('images/quizq5incorrect.png')
quizResults0CorrectBg = pygame.image.load('images/quizresults0.png')
quizResults1CorrectBg = pygame.image.load('images/quizresults1.png')
quizResults2CorrectBg = pygame.image.load('images/quizresults2.png')
quizResults3CorrectBg = pygame.image.load('images/quizresults3.png')
quizResults4CorrectBg = pygame.image.load('images/quizresults4.png')
quizResults5CorrectBg = pygame.image.load('images/quizresults5.png')
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
numberOfCorrect = 0

# Necessary for python to work on tdsb computers
if platform.system() == 'Windows':
    os.environ['SDL_VIDEODRIVER'] = 'windib'

# Define functions
# Function for the title screen
def titleScreen():
    gameExit = False

    gameDisplay = pygame.display.set_mode((800, 600)) # Set display size
    pygame.display.set_caption('Wildlife Survival Guide') # Set caption at top to Wildlife Survival Guide
    pygame.display.set_icon(icon) # Sets icon   
    
    # Set background
    gameDisplay.blit(titleScreenBg, (0, 0)) 
    
    # Background music
    mixer.music.load('music/DynamiteInstrumental.mp3')
    mixer.music.play(-1) # -1 is to keep the music looping     
    
    pygame.display.update()
    
    clock.tick(60) 
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if x >= 524 and x <= 751:
                    if y >= 477 and y <= 548:
                        mainMenu()  
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()

# Function for the main menu
def mainMenu():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))
    
    # Set background
    gameDisplay.blit(mainMenuBg, (0, 0)) 
    
    # Display buttons
    gameDisplay.blit(storyButton, (43, 264))
    gameDisplay.blit(instructionsButton, (286, 264))
    gameDisplay.blit(lessonButton, (529, 264))
    gameDisplay.blit(quizButton, (43, 378))
    gameDisplay.blit(quizResultsButton, (286, 378))
    gameDisplay.blit(exitButton, (529, 378))        
    pygame.display.update()
    
    clock.tick(60)      
    
    global numberOfCorrect
    
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
                        quiz()
                elif x >= 286 and x <= 513:
                    if y >= 264 and y <= 336:
                        instructions()
                    elif y >= 378 and y <= 449:
                        if numberOfCorrect == 0:
                            quizResults0()
                        elif numberOfCorrect == 1:
                            quizResults1()
                        elif numberOfCorrect == 2:
                            quizResults2()                          
                        elif numberOfCorrect == 3:
                            quizResults3()
                        elif numberOfCorrect == 4:
                            quizResults4()
                        elif numberOfCorrect == 5:
                            quizResults5()                            
                elif x >= 529 and x <= 756:
                    if y >= 264 and y <= 336:
                        lesson()
                    elif y >= 378 and y <= 449:
                        quit()
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()            

# Function for the animation                
def animation():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(animationBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            event = pygame.event.get()
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1] 
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 505 and y <= 575:
                    if x >= 547 and x <= 773:
                        animation1()
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()              

# Function for Part 1 of the animation                        
def animation1():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(animation1Bg, (0, 0)) # Sets background image
    pygame.display.update()
    clock.tick(60)   
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        animation2s1()
                    elif x >= 513 and x <= 740:
                        animation2s2()
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()                      

# Function for part 2 scenario 1 of the animation                            
def animation2s1():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(animation2s1Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        animation3()
                    elif x >= 513 and x <= 740:
                        ending1()                
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()                  

# Function for part 2 scenario 2 of the animation    
def animation2s2():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(animation2s2Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]   
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        ending2()
                    elif x >= 513 and x <= 740:  
                        animation21()
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()                  
                            
# Function for part 2.1 of the animation
def animation21():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(animation21Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        animation3()
                    elif x >= 513 and x <= 740:
                        ending1()   
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()                      
    
# Function for part 3 of the animation
def animation3():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(animation3Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)   
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        ending3() 
                    elif x >= 513 and x <= 740:
                        animation4() 
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()                  

# Function for part 4 of the animation                            
def animation4():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(animation4Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        ending4()
                    elif x >= 513 and x <= 740:
                        animation5()    
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()                      
                            
# Function for part 5 of the animation
def animation5():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(animation5Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)     
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 513 and x <= 740:
                        ending5()    
    
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()          

# Function for ending 1 of the animation
def ending1():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(animationEnding1Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)  
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        mainMenu()
                    elif x >= 513 and x <= 740:
                        quit() 
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()                              

# Function for ending 2 of the animation                            
def ending2():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(animationEnding2Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)   
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        mainMenu()
                    elif x >= 513 and x <= 740:
                        quit()
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()                              

# Function for ending 3 of the animation                            
def ending3():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(animationEnding3Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        mainMenu()
                    elif x >= 513 and x <= 740:
                        quit()
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()                              

# Function for ending 4 of the animation                            
def ending4():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(animationEnding4Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        mainMenu()
                    elif x >= 513 and x <= 740:
                        quit()        
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()              

# Function for ending 5 of the animation                            
def ending5():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(animationEnding5Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)    
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 483 and y <= 554:
                    if x >= 60 and x <= 287:
                        mainMenu()
                    elif x >= 513 and x <= 740:
                        quit() 
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()                            
                            
# Function for the instructions
def instructions():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(instructionsBg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)  
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]    
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        mainMenu()    
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()                                                    

# Function for the lesson                
def lesson():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(lesson1Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]    
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        mainMenu()
                    elif x >= 524 and x <= 751:
                        lesson2()
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()               

# Function for the second part of the lesson                            
def lesson2():
    gameExit = False 
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(lesson2Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60) 
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        lesson()
                    elif x >= 524 and x <= 751:
                        citations1()
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()              

# Function for the first part of the citations                            
def citations1():
    gameExit = False 
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(citations1Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        lesson2()
                    elif x >= 524 and x <= 751:
                        citations2() 
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()              
                        

# Function for the second part of the citations                            
def citations2():
    gameExit = False 
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(citations2Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)

    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        citations1()
                    elif x >= 524 and x <= 751:
                        citations3()  
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()                                  

# Function for the third part of the citations
def citations3():
    gameExit = False 
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(citations3Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        citations2()
                    elif x >= 524 and x <= 751:
                        citations4()  
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()                         

# Function for the fourth part of the citations                            
def citations4():
    gameExit = False 
    gameDisplay = pygame.display.set_mode((800, 600))   
    gameDisplay.blit(citations4Bg, (0, 0)) # Set background image
    pygame.display.update()
    clock.tick(60)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        citations3()
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()            

# Function for the quiz instructions
def quiz():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizInstructionsBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)    
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:
                        mainMenu()
                    if x >= 524 and x <= 751:
                        quizQ1()
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()                  

# Function for question 1 of the quiz
def quizQ1():
    gameExit = False
    global quizQuestionsCorrect
    quizQuestionsCorrect = int(0)
    
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizQuestion1Bg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)    
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if x >= 60 and x <= 740:
                    if y >= 207 and y <= 278:
                        quizQ1Correct()
                    elif y >= 295 and y <= 366:
                        quizQ1Incorrect()
                    elif y >= 385 and y <= 456:
                        quizQ1Incorrect()                  
                    elif y >= 474 and y <= 545:
                        quizQ1Incorrect()                             
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()  

# Function for if user gets question 1 correct                
def quizQ1Correct():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizQuestion1CorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)   
    
    global numberOfCorrect
    numberOfCorrect += 1  
    print(numberOfCorrect)
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 524 and x <= 751:
                        quizQ2()    
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()              

# Function for if user gets question 1 incorrect    
def quizQ1Incorrect():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizQuestion1IncorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)  
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 524 and x <= 751:
                        quizQ2()    
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()                          

# Function for question 2    
def quizQ2():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizQuestion2Bg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)    
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if x >= 60 and x <= 740:
                    if y >= 207 and y <= 278:
                        quizQ2Incorrect()
                    elif y >= 295 and y <= 366:
                        quizQ2Incorrect()
                    elif y >= 385 and y <= 456:
                        quizQ2Correct()                  
                    elif y >= 474 and y <= 545:
                        quizQ2Incorrect()                             
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()  

# Function for if user gets question 2 correct                
def quizQ2Correct():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizQuestion2CorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)   
    
    global numberOfCorrect
    numberOfCorrect += 1  
    print(numberOfCorrect)    
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 524 and x <= 751:
                        quizQ3()    
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()              

# Function for if user gets question 2 incorrect    
def quizQ2Incorrect():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizQuestion2IncorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)  
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 524 and x <= 751:
                        quizQ3()    
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()              
                        
# Function for question 3   
def quizQ3():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizQuestion3Bg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)  
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if x >= 60 and x <= 740:
                    if y >= 207 and y <= 278:
                        quizQ3Incorrect()
                    elif y >= 295 and y <= 366:
                        quizQ3Correct()
                    elif y >= 385 and y <= 456:
                        quizQ3Incorrect()                  
                    elif y >= 474 and y <= 545:
                        quizQ3Incorrect()                             
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()  

# Function for if user gets question 3 correct                
def quizQ3Correct():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizQuestion3CorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)   
    
    global numberOfCorrect
    numberOfCorrect += 1  
    print(numberOfCorrect)        
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 524 and x <= 751:
                        quizQ4()    
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()              

# Function for if user gets question 3 incorrect    
def quizQ3Incorrect():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizQuestion3IncorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)  
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 524 and x <= 751:
                        quizQ4()  
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()              

# Function for question 4                        
def quizQ4():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizQuestion4Bg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)  
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if x >= 60 and x <= 740:
                    if y >= 207 and y <= 278:
                        quizQ4Incorrect()
                    elif y >= 295 and y <= 366:
                        quizQ4Incorrect()
                    elif y >= 385 and y <= 456:
                        quizQ4Correct()                  
                    elif y >= 474 and y <= 545:
                        quizQ4Incorrect()                             
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()  

# Function for if user gets question 4 correct                
def quizQ4Correct():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizQuestion4CorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)   
    
    global numberOfCorrect
    numberOfCorrect += 1  
    print(numberOfCorrect)            
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 524 and x <= 751:
                        quizQ5()    
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()              

# Function for if user gets question 4 incorrect    
def quizQ4Incorrect():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizQuestion4IncorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)  
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 524 and x <= 751:
                        quizQ5()  
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()    

# Function for question 5                
def quizQ5():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizQuestion5Bg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)    
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if x >= 60 and x <= 740:
                    if y >= 207 and y <= 278:
                        quizQ5Incorrect()
                    elif y >= 295 and y <= 366:
                        quizQ5Incorrect()
                    elif y >= 385 and y <= 456:
                        quizQ5Correct()                  
                    elif y >= 474 and y <= 545:
                        quizQ5Incorrect()                             
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()  

# Function for if user gets question 5 correct                
def quizQ5Correct():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizQuestion5CorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)   
    
    global numberOfCorrect
    numberOfCorrect += 1  
    print(numberOfCorrect)            
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 524 and x <= 751:
                        if numberOfCorrect == 0:
                            quizResults0()
                        elif numberOfCorrect == 1:
                            quizResults1()
                        elif numberOfCorrect == 2:
                            quizResults2()                           
                        elif numberOfCorrect == 3:
                            quizResults3()
                        elif numberOfCorrect == 4:
                            quizResults4()
                        elif numberOfCorrect == 5:
                            quizResults5() 
                        
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()              

# Function for if user gets question 5 incorrect    
def quizQ5Incorrect():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizQuestion5IncorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)  
    
    global numberOfCorrect
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 524 and x <= 751:
                        if numberOfCorrect == 0:
                            quizResults0()
                        elif numberOfCorrect == 1:
                            quizResults1()
                        elif numberOfCorrect == 2:
                            quizResults2()                          
                        elif numberOfCorrect == 3:
                            quizResults3()
                        elif numberOfCorrect == 4:
                            quizResults4()
                        elif numberOfCorrect == 5:
                            quizResults5()                         
                            
            if ev.type == pygame.QUIT:
                gameExit = True
                pygame.quit()        

# Function for if the user gets zero correct on the quiz                
def quizResults0():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizResults0CorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)      
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:    
                        mainMenu()

# Function for if the user gets one correct on the quiz 
def quizResults1():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizResults1CorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)      
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:    
                        mainMenu()
                        
# Function for if the user gets two correct on the quiz 
def quizResults2():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizResults2CorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)      
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:    
                        mainMenu()
                        
# Function for if the user gets three correct on the quiz 
def quizResults3():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizResults3CorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)      
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:    
                        mainMenu()           
                        
# Function for if the user gets four correct on the quiz 
def quizResults4():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizResults4CorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)      
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:    
                        mainMenu()                        
                        
# Function for if the user gets five correct on the quiz 
def quizResults5():
    gameExit = False
    gameDisplay = pygame.display.set_mode((800, 600))  
    gameDisplay.blit(quizResults5CorrectBg, (0, 0)) # Set background image
    pygame.display.update()   
    clock.tick(60)      
    
    while not gameExit:
        for ev in pygame.event.get():
            clickPos = pygame.mouse.get_pos()
            x = clickPos[0]
            y = clickPos[1]
            
            # Check if where the user clicked is in the range of a button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if y >= 477 and y <= 548:
                    if x >= 48 and x <= 275:    
                        mainMenu()                        

# Display the title screen when the program runs
titleScreen()
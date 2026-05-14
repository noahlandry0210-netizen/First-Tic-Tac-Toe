""" Noah Landry Tik-Tac-Toe ISU
The purpose of this assignment is to be able to play the game tic-tac-toe using python and pygame.
the program should be able to allow players to play against eachother and ensure that
no illegal moves are happening. The program features changing colours, win detection and a scoring system."""

#functions
def winner(c_board):
    
    # all possible win conditions
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    # goes through each item in wins, which is also a list of all the possible win scenarios
    
    for thing in wins:#after each loop it is set to then next index in the wins list
        
        # this if statement checks for each possible win combination and checks that the same symbol is in that win
        if c_board[thing[0]] == c_board[thing[1]] == c_board[thing[2]] and c_board[thing[0]] != " " :
            ## return the symbol that won
            return c_board[thing[0]]

        
    ## if no winner,  returns XO
    if " " not in c_board:#checks to see if board is full
        return "XO"
    return None#if not full, return None




    
def write(string, colour, x, y, size): # this function will be used to write text on the screen

    # the first argument is the font. I dont have any fonts, so None will use the default font
    # second argument is text size
    font = pygame.font.SysFont(None, size)

    
    #passing in what I want the text to display
    text = font.render(string, True, colour) # the boolean is Anti-aliasing and last argment is the colour

    screen.blit(text, (x, y))#update it on screen

def button(x, y, width, height, colour):# use this to create  a button

    #draw the rectangle
    button = pygame.draw.rect(screen, colour, pygame.Rect(x, y, width, height), 2)#what surface, colour, position, width and height

    
    
    
    #I realise that I could have just typed out pygame.draw.rect but I thought prior to using pygame it would need more lines



def is_clicked(x, y, width, height):

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#check to see if mouse is clicked
        
        #check to see if mouse is within the coordinates passed in 
        return x < mouseX < x+width and y < mouseY < y+height


    

def drawTIC(c): # draw the tic tac toe board, the argument is the colour of the lines

    width  = 250
    length = 50
    


    #first tuple is the position at which the line starts drawing, the second where is stops
    pygame.draw.line(screen, c, (250, 50), (250, 550), 5) #first vertical line
    #surface, colour, start, end, thickness
    pygame.draw.line(screen, c, (417, 50), (417, 550), 5) #second vertical line

    pygame.draw.line(screen, c, (83, 217), (584, 217), 5) #first horizontal line

    pygame.draw.line(screen, c, (83, 384), (584, 384), 5) #second horizontal line


    


    #x, y, width, height, colour
    
    

def CheckAndDraw():# this function will draw the buttons for the board and check if they are clicked
    
        temp = 0

        tempX = 83# top left X starting position to draw boxes
        
        tempY = 50#top left Y starting position to draw boxes

        
        box = 0


        
        
        for n in range(3):#these 2 for loops will draw the boxes in a 3x3 box
            for i in range(3):

                box +=1
                
                button(tempX, tempY, 167, 167, "white")#outline of box will be set to white so it blends into the background. If another colour, it would show squares in each box

                #x, y, width, height
                if is_clicked(tempX, tempY, 167, 167) == True:
                    TEMP = box-1 #set the temp variable to what box the user clicked
                    return TEMP
                
                
                
                tempX += 167
            tempX = 83
            tempY += 167



def drawChanges():#checks the board for changes and updates the position of X's and O's


    
    
    for i in range(len(board)):
        if board[i] == "X":
            DrawX(i)
        elif board[i] == "O":
            DrawO(i)



def DrawX(boxx):#Draw an X in the box that the user clicks   

    

    tempX = 83+(67//2)#this function is all similar logic to the DrawX() function
    tempY = 50+(67//2)

##    tempX = 83#top left starting position
##    tempY = 50#top left starting position
    #size = 167
    

    #if boxx <= 2:
        

    if boxx <= 5 and boxx >= 3:

        tempY += 167
        boxx -=3#change boxx by -3 because then it will be in a range of 0-2

        #pygame.draw.line(screen, Xcolour, (tempX+167*boxx, tempY), (tempX+167+167*boxx, tempY+167), 10)#must shift over 1 box. 1 box is ~167 pixels
        #pygame.draw.line(screen, Xcolour, (tempX+167+167*boxx, tempY), (tempX+167*boxx, tempY+167),10)
        
    elif boxx >= 6 and boxx <= 8:

        tempY += 167*2
        boxx -=6 #same logic as above where boxx was changed by -3. Now that it is in the last row, it needs to be changed by -6

    pygame.draw.line(screen, Xcolour, (tempX+167*boxx, tempY), (tempX+100+167*boxx, tempY+100), 10)
    pygame.draw.line(screen, Xcolour, (tempX+100+167*boxx, tempY), (tempX+167*boxx, tempY+100), 10)



#previous logic

##    if boxx <= 2:
##        pygame.draw.line(screen, Xcolour, (tempX+167*boxx, tempY), (tempX+167+167*boxx, tempY+167), 10)
##        pygame.draw.line(screen, Xcolour, (tempX+167+167*boxx, tempY), (tempX+167*boxx, tempY+167), 10)
##
##    elif boxx <= 5 and boxx >= 3:
##
##        tempY += 167
##        boxx -=3#change boxx by -3 because then it will be in a range of 0-2
##
##        pygame.draw.line(screen, Xcolour, (tempX+167*boxx, tempY), (tempX+167+167*boxx, tempY+167), 10)#must shift over 1 box. 1 box is ~167 pixels
##        pygame.draw.line(screen, Xcolour, (tempX+167+167*boxx, tempY), (tempX+167*boxx, tempY+167),10)
##        
##    elif boxx >= 6 and boxx <= 8:
##
##        tempY += 167*2
##        boxx -=6 #same logic as above where boxx was changed by -3. now that it is in the last row, it needs to be changed by -6
##
##        pygame.draw.line(screen, Xcolour, (tempX+167*boxx, tempY), (tempX+167+167*boxx, tempY+167), 10)
##        pygame.draw.line(screen, Xcolour, (tempX+167+167*boxx, tempY), (tempX+167*boxx, tempY+167),10)


def DrawO(boxx):#Draw an O in the box that the user clicks

    tempX = 83+(167//2)#this function is all similar logic to the DrawX() function
    tempY = 50+(167//2)
    
    #if boxx <= 2:
        #pygame.draw.circle(screen, Ocolour, (tempX+167*boxx, tempY), 50, 5)#must shift over 1 box. 1 box is ~167 pixels
        

    if boxx <= 5 and boxx >= 3:

        tempY += 167
        boxx -=3
        
        #pygame.draw.circle(screen, Ocolour, (tempX+167*boxx, tempY), 50, 5)

    elif boxx >= 6 and boxx <= 8:

        tempY += 167*2
        boxx -=6
        
        #pygame.draw.circle(screen, Ocolour, (tempX+167*boxx, tempY), 50, 5)
    pygame.draw.circle(screen, Ocolour, (tempX+167*boxx, tempY), 50, 5)



    


###main script

##
##board = [" "]*9# the list that keeps track of board changes
##place = None# this will be used to track where the player wants to place their X/O
##for i in range(len(board)):
##
##    #printing the board, used to test before implementing pygame
##    print(board[0:3])
##    print(board[3:6])
##    print(board[6:9])
##
##    
##    if i % 2 == 0:
##        print("X TURN! Choose 0-8")
##        while True: # keep running until it is a valid place to place
##            place = int(input("Where would you like your symbol to go? 0-8"))
##            if board[place] != " ":
##                continue
##            else:
##                break
##
##        board[place] = "X"
##
##    
##    else:
##        print("O TURN! Choose 0-8")
##        while True: # keep running until it is a valiud place to place
##            place = int(input("Where would you like your symbol to go? 0-8"))
##            if board[place] != " ":
##                continue
##            else:
##                break
##        board[place] = "O"
        
##    

    
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True


pygame.display.set_caption("Tic-Tac-Toe Noah Landry")

state = "menu"



colours = ["black", "red", "orange", "yellow", "green", "blue", "indigo", "violet"]#black + ROY G BIV

Xcolour = colours[0] #X will start at black, the default colour

Ocolour = colours[0] # O will start at black, the default colour

theme = "black"#black(default), this is going to be used to change the game theme colour

turn = 0#going to be used in a for loop to calculate whos turn it is

board = [" "]*9# the list that keeps track of board changes

score = [0, 0]#first is X, second is O

#TEMP = None #using this variable to check if button registers click in board

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    
    for event in pygame.event.get():# this for loop runs whenever there is a user input

        
        if event.type == pygame.QUIT:
            running = False

    

        mouseX, mouseY = pygame.mouse.get_pos()



        if state == "X wins" or state == "O wins" or state == "draw":#this is the restart button
            if is_clicked(290, 550, 100, 60) == True:
                state = "menu"
                continue
        


        #the menu screen 
        if state == "menu":

            #these variables are set again so that the player can restart the game with a new board(after playing a game)
            board = [" "]*9
            turn = 0
            

            if is_clicked(310, 550, 100, 60):
                state = "game"
            
            
            #print(is_clicked(310, 550, 100, 60)) # used to test functionality of the new function is_clicked



            #checking if clicked for theme colour buttons
            if is_clicked(50, 150, 100, 60):#black option
                theme = "black"


            if is_clicked(50, 250, 100, 60):#red option
                theme = "red"


            if is_clicked(50, 350, 100, 60):#orange option
                theme = "orange"

            if is_clicked(50, 450, 100, 60):#yellow option
                theme = "yellow"

            if is_clicked(50, 550, 100, 60):#green option
                theme = "green"


            #these will check if the changing colours for symbol buttons are clicked
            if is_clicked(220, 250, 100, 60):#X option

                #find the index at which Xolour was previosuly and add 1
                Xcolour = colours[(colours.index(Xcolour)+1)%8]#mod 8 so that it loops back to the start of the colours[] list

            if is_clicked(400, 250, 100, 60):#O option
                #same logic as Xcolour
                Ocolour = colours[(colours.index(Ocolour)+1)%8]
            

            
            
            

        #the game screen
        if state == "game":

            

            
            box = CheckAndDraw()
            
            if box != None:#this is the turn systems, it will also update the board[] list
                if turn%2 == 0:#X turn
                    
                    
                    if board[box] == "X" or board[box] == "O":#this checks if the box the user clicks is already occupied
                        continue#go back to top of loop without changing turn
                    
                    board[box] = "X"

                    
                    turn += 1#change turn by one so next time the loop will detect it is O turn
                else:#O turn
                    
                    if board[box] == "X" or board[box] == "O":#same as above, checking if occupied
                        
                        continue#go back to top if already occupied
                    
                    board[box] = "O"
                    
                    turn +=1

            #this runs after the user clicks a valid box
            #if none of these happens, game will still continue
            winners = winner(board)
            if winners == "X":#X wins
                state = "X wins"
                score[0] += 1#score at 0 is X
                
            elif winners == "O":#O wins
                state = "O wins"
                score[1] += 1#score at 1 is O

                
            elif winners == "XO":#draw
                state = "draw"
                score[0] += 0.5#chess system, add 0.5 to each play for a dar
                score[1] += 0.5

                

            

                

                

        

    #everything here will run every frame(60 fps)



    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    
    if state == "menu":
        #write text on the screen
            
            write("Tic-Tac-Toe", theme, 220, 50, 74)#title of game
            write("X:"+ str(score[0]), theme, 220, 360, 74)#scores
            write("O:"+ str(score[1]), theme, 400, 360, 74)

            
            #x, y, width, height, colour
            button(310, 550, 100, 60, "black")
            
            write("PLAY", "green", 335, 573, 30)# add text to the button





            #draw the different options of theme colours
            button(50, 150, 100, 60, "black")#black button option
            write("BLACK", "black", 75, 170, 30)

            button(50, 250, 100, 60, "red")#red button option
            write("RED", "red", 75, 270, 30)

            button(50, 350, 100, 60, "orange")#orange button option
            write("ORANGE", "orange", 55, 370, 30)

            button(50, 450, 100, 60, "yellow")#yellow button option
            write("YELLOW", "yellow", 55, 470, 30)

            button(50, 550, 100, 60, "green")#green button option
            write("GREEN", "green", 70, 570, 30)

            write("THEME: "+theme.upper(), theme, 310, 673, 30)#tell user the theme selected



            #give X and o the option to change their own colour
            button(220, 250, 100, 60, Xcolour)
            write("X COLOUR", Xcolour, 225, 270, 25)


            button(400, 250, 100, 60, Ocolour)
            write("O COLOUR", Ocolour, 405, 270, 25)
            

    if state == "game":

        #all of these must be called and drawn every frame
        
        #the order at which the functions are called matters. If drawTic wasnt called last, then the boxes for each square would appear above the board
        CheckAndDraw()#these functions will show up alot farther down aswell
        drawChanges()
        drawTIC(theme)

        write("X:"+ str(score[0]), theme, 220, 650, 74)#want the user to also see the scores in game
        write("O:"+ str(score[1]), theme, 400, 650, 74)


        
        


        

    if state == "X wins":
        write("X WINS", theme, 250, 650, 74)

        button(290, 550, 100, 60, theme)
            
        write("MENU", theme, 315, 573, 30)# add text to the button
        
        

        

        #show board after game
        drawChanges()
        drawTIC(theme)
        

    if state == "O wins":
        write("O WINS", theme, 250, 650, 74)


        button(290, 550, 100, 60, theme)
            
        write("MENU", "green", 315, 573, 30)# add text to the button        


        #same reason as above
        drawChanges()
        drawTIC(theme)
        
        

    if state == "draw":
        write("DRAW", theme, 250, 650, 74)



        button(290, 550, 100, 60, theme)
            
        write("MENU", "green", 315, 573, 30)# add text to the button
        
        #same reason as above
        drawChanges()
        drawTIC(theme)
        

        #CheckAndDraw()

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
    

# -*- coding: utf-8 -*-
"""
Created on Thu May 24 15:47:03 2018

@author: ggoncalves
"""
import pygame

#Defir matrizes
explorado = []; #Inicia o conjunto explorado como vazio
caminho = []; #Inicia o caminho como vazio
fronteira = [];
ini = [];   #Inicio do caminho
end = [];   #Final do caminho

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

NADA = 0
PLAYER = 1
PC = 2
 
# This sets the margin between each cell
MARGIN = 5

# This sets the number of squares in column and row
SQUARE_NUMBER_ROW = 3
SQUARE_NUMBER_COLUMN = 3

# This sets the WIDTH and HEIGHT of window
WINDOW_WIDTH = 255
WINDOW_HEIGHT = 255

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 78 #(WINDOW_WIDTH/SQUARE_NUMBER_COLUMN) - MARGIN*1.5 #78 Precisa ver como arredondar para cima
HEIGHT = 78 #(WINDOW_HEIGHT/SQUARE_NUMBER_ROW) - MARGIN*1.5 #78 Precisa ver como arredondar para cima

 
#Botoes
LEFT_CLICK = 1
MIDLE_CLICK = 1
RIGHT_CLICK = 3

#Turns
PC_TURN = 1
PLAYER_TURN = -1


# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(SQUARE_NUMBER_ROW):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(SQUARE_NUMBER_COLUMN):
        grid[row].append(0)  # Append a cell
    
    # Set row 1, cell 5 to one. (Remember rows and
    # column numbers start at zero.)
    #grid[1][5] = 1
    
def jogada_PC():
    
    return

def main():

    global column;
    global row;
    
    # Initialize pygame
    pygame.init()
     
    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [WINDOW_WIDTH, WINDOW_HEIGHT]
    screen = pygame.display.set_mode(WINDOW_SIZE)
     
    # Set title of screen
    pygame.display.set_caption("Algoritmo de busca")
     
    #button = pygame.Rect(300, 200, 50, 25)
    
    # Loop until the user clicks the close button.
    done = False
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    #Contagem para saber quando é o click de começo e fim
    player = 1
    
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print( event.button )
                if ( event.button == LEFT_CLICK ):
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    if ( column >= 10 ):
                        break;
                    
                    print("Click ", pos, "Grid coordinates: ", row, column)
                    if ( PC_TURN == player and grid[row][column] == NADA ):
                        grid[row][column] = PC;
                        ini.append(column);
                        ini.append(row);
                        player *= (-1);
                        #jogada_PC();
                    elif ( PLAYER_TURN == player and grid[row][column] == NADA  ):
                        grid[row][column] = PLAYER;
                        end.append(column);
                        end.append(row);
                        player *= (-1)
                    
        # Set the screen background
        screen.fill(BLACK)
        
        #pygame.draw.rect(screen, [125, 125, 125], button)  # draw button
        
        # Draw the grid
        for row in range(SQUARE_NUMBER_ROW):
            for column in range(SQUARE_NUMBER_COLUMN):
                color = WHITE
                if grid[row][column] == PLAYER:
                    color = BLUE
                elif grid[row][column] == PC:
                    color = RED
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
     
        # Limit to 60 frames per second
        clock.tick(60)
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
    return

#INIT programa
main();

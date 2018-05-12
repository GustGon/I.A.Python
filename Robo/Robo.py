# -*- coding: utf-8 -*-
"""
Created on Sat May 12 11:36:12 2018

@author: gugon
"""
import pygame

#Defir matrizes
explorado = []; #Inicia o conjunto explorado como vazio
caminho = []; #Inicia o caminho como vazio
fronteira = [];
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

COMECO = 1
FIM = 2
OBSTACULO = 3
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
#grid[1][5] = 1
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Contagem para saber quando é o click de começo e fim
count = 1
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
                
            # Set that location to one
            grid[row][column] = count
            print("Click ", pos, "Grid coordinates: ", row, column)
            if ( COMECO == count ):
                ini = [column,row]
                count += 1
            elif ( FIM == count ):
                end = [column,row]
                count += 1

 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == COMECO:
                color = BLUE
            elif grid[row][column] == FIM:
                color = BLACK
            elif grid[row][column] == OBSTACULO:
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


def encontraCaminho(ini, end):
    
    G = 1
    H = getDistValue(ini, end)
    F = G + H 
    node = [ini, ini, G, H, F]
    custo = 0

    if(node[0] == end):
        print('O n de inicio ja é o nó de destino.');
        return
    
    fronteira.append(node); #[Nó, NóPai, pesoCaminho, dist, soma]

    while(fronteira):
        
        node = fronteira.pop(maisBarato(fronteira)) #Nó mais leve da fronteira.
        
        explorado.append(node)  #Adiciona no  explorados o nó analisado.
        
        if( node[0] == end):
            return solucao(ini)    
        
        tabelaPeso = mapa[mapa[node[0]]>0][node[0]]    #possiveis caminhos com respectivos pessos
        opcoes = list(tabelaPeso.index.values)         #opcoes com apenas seus nomes

        for filho in opcoes:    #Possiveis caminhos a seguir a partir do nó.
            
            G = 1;
            H = getDistValue(filho);
            F = G + H;
            filhoCompleto = [filho, node[0], G, H, F]
            colum = 2
            row = 2
            
            if ( not isExplorado(filho) ):
                
                G_tempF = G + custo
            
            elif( ( not fronteira.count(filhoCompleto) > 0 ) and
                 not( 0 > colum > WIDTH or 0 > row > HEIGHT ) ):
                    
                fronteira.append(filhoCompleto)
                G_F = G_tempF
                #F_F = G_F + H
                #custo += F_F

            elif( G_F > G_tempF ):
                
                G_F = G_tempF
                #F_F = G_F + H
    
    return

def isExplorado(filho): #Verifica se a cidade ja foi explorada
    isEx = False;
    
    for ex in explorado:
        if (ex[0] == filho):
            isEx = True;
            break;
    return isEx

def maisBarato(fronteira):  #Get da fronteira com o pesso menor;
    
    ref = 1000000000000
    
    for k in range(0,len(fronteira)):
        peso = fronteira[k][4]
        if ( peso < ref ):
            ref = peso
            maisBarato = k
            
    return maisBarato

def solucao(ini):   #Mostra a rota das cidades e o custo total por passar por elas;

    custoCaminho = 0
    menor = []
    menor.append(explorado[len(explorado) - 1][0])  #Nó filho
    
    proximo = explorado[len(explorado) - 1][0]#Nó pai de origem
    
    for n in range(len(explorado) - 1,0,-1):    #Varrer todos as cidades exploradas
        if ( explorado[n][0] == proximo ):
            menor.append(explorado[n][1])
            proximo = explorado[n][1]
            custoCaminho += explorado[n][2]
        if ( proximo == ini ):  #Encontrado o destino
            break
    
    for p in range(len(menor) - 1,-1,-1):   #Ajusta o caminho na sequencia
        caminho.append(menor[p])    

    return print(caminho, '\n\nCusto do Caminho:',custoCaminho )

def getDistValue(ini, end):   #Valor na tabela dist
    deltaColun = ini[0] - end[0]
    deltaRow = ini[1] - end[1]
    dist = (deltaColun**2 + deltaRow**2)**(1/2)
    return dist

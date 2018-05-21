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
BLACK_GREEN = (0, 125, 0)
LIGTH_GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ALGUMA = (125, 125, 125)

NADA = 0
COMECO = 1
FIM = 2
OBSTACULO = 3
FRONTEIRA = 4
EXPLORADO = 5
CAMINHO = 6
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

 
# This sets the margin between each cell
MARGIN = 5
 
#Botoes
LEFT_CLICK = 1
MIDLE_CLICK = 1
RIGHT_CLICK = 3


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
        
        opcoes = getAcoes(node)         #opcoes com apenas seus nomes
        
        explorado.append(node)  #Adiciona no  explorados o nó analisado.
        
        quadrado = grid[node[0][1]][node[0][0]]
        if ( quadrado == FRONTEIRA ):
            grid[node[0][1]][node[0][0]] = EXPLORADO
        
        if( node[0] == end):
            return solucao(ini)    

        for filho in opcoes:    #Possiveis caminhos a seguir a partir do nó.
            
            G = 1;
            H = getDistValue(filho, end);
            F = G + H;
            filhoCompleto = [filho, node[0], G, H, F]
            column = filho[1]
            row = filho[0]
            
            if ( not isExplorado(filho) ):
                
                G_tempF = G + custo
            
                if( not fronteira.count(filhoCompleto) > 0 ):
                        
                    fronteira.append(filhoCompleto)
                    grid[column][row] = FRONTEIRA
                    G_F = G_tempF
                    #F_F = G_F + H
                    #custo += F_F
    
                elif( G_F > G_tempF ):
                    
                    G_F = G_tempF
                    #F_F = G_F + H
    
    return

def getAcoes(local):
    
    baixo = [local[0][0], local[0][1] + 1]
    cima =  [local[0][0], local[0][1] - 1]
    esquerda = [local[0][0] - 1, local[0][1]]
    direita = [local[0][0] + 1, local[0][1]]
    
    opcoes = []

    if ( not ((0 > cima[0]) or (cima[0] > row) or (0 > cima[1]) or (cima[1] > row)) and
        (grid[cima[1]][cima[0]] == NADA or 
         grid[cima[1]][cima[0]] == FIM)):
        opcoes.append(cima);
                    
    if ( not ((0 > baixo[0]) or (baixo[0] > row) or (0 > baixo[1]) or (baixo[1] > row)) and
        (grid[baixo[1]][baixo[0]] == NADA or 
         grid[baixo[1]][baixo[0]] == FIM)):
        opcoes.append(baixo);
            
    if ( not ((0 > esquerda[0]) or (esquerda[0] > row) or (0 > esquerda[1]) or (esquerda[1] > row)) and
        (grid[esquerda[1]][esquerda[0]] == NADA or 
         grid[esquerda[1]][esquerda[0]] == FIM)):
        opcoes.append(esquerda);

    if ( not ((0 > direita[0]) or (direita[0] > row) or (0 > direita[1]) or (direita[1] > row)) and
        (grid[direita[1]][direita[0]] == NADA or 
         grid[direita[1]][direita[0]] == FIM)):
        opcoes.append(direita);
    
    return opcoes

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
            
    for c in caminho:
        quadrado = grid[c[1]][c[0]]
        if( quadrado == EXPLORADO ):
            grid[c[1]][c[0]] = CAMINHO
    

    return print(caminho, '\n\nCusto do Caminho:',custoCaminho )

def getDistValue(ini, end):
    #Heuclidiana
    deltaColun = ini[0] - end[0]
    deltaRow = ini[1] - end[1]
    dist = (deltaColun**2 + deltaRow**2)**(1/2)
    return dist

def main():

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
                print( event.button )
                if ( event.button == LEFT_CLICK ):
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    if ( column >= 10 ):
                        break;
                    # Set that location to one
                    grid[row][column] = count
                    print("Click ", pos, "Grid coordinates: ", row, column)
                    if ( COMECO == count ):
                        grid[row][column] = COMECO;
                        ini = [column,row]
                        count += 1
                    elif ( FIM == count ):
                        grid[row][column] = FIM;
                        end = [column,row]
                        count += 1
                elif ( event.button == RIGHT_CLICK ):
                    encontraCaminho(ini, end);
    
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
                elif grid[row][column] == FRONTEIRA:
                    color = BLACK_GREEN
                elif grid[row][column] == EXPLORADO:
                    color = LIGTH_GREEN
                elif grid[row][column] == CAMINHO:
                    color = ALGUMA
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

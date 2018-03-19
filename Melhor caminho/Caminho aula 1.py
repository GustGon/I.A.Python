''' Aula Inteligencia Artificial '''
import csv

#Matriz de caminhos e custos.
#Pegar pelo excel ou fazer na mao


def bfd(A,ini,fim):

    node = ini
    custo = 0

    if(node == fim):
        caminho = 0;
        custo = 0;
        print('O n de inicio ja é o nó de destino.');
        return
    

    fronteira  = [ini, ini, 0]; #[Nó, Nó_Pai, Custo]
    explorado = []; #Inicia o conjunto explorado como vazio
    caminho = []; #Inicia o caminho como vazio

    while(fronteira):
        

        '''
        seu condigo aki
        se FRONTEIRA = VAZIO entao retorne FALHA
        nó <- POP(FRONTEIRA) /escolhe o nó mais razo da fronteira
        adiciona NÓ a EXPLORADO
        para cada ACAO em ACOES(NÓ) faça
            FILHO <- FILHO-NÓ(problema,NÓ,AÇÃO)
            se FILHO não esta em EXPLORADO ou FRONTEIRA entao
                se FILHO = OBJETIVO entao retorne SOLUÇÃO(FILHO)
                FRONTEIRA <- INSERIR(FILHO, FRONTEIRA)
        '''
        
    if(not fronteira):
        caminho = -1
        custo = -1
        print("Não foi possível encontrar um caminho do nó de início ao nó de destino.")
        return
    return    

print ("Começou")
mapa = open('mapa.csv','rb')

reader = csv.reader(mapa)

A = []
for linha in mapa:
    print (linha)
    A += linha

print (A)

A 
    #bfd(mapa,0,8)


'''

function [caminho, custo] = bfs(A,ini,fim)

node = ini;
custo = 0;

if(node == fim)
    caminho = 0;
    custo = 0;
    disp('O n� de in�cio j� � o n� de destino.');
    return
end

fronteira  = [ini ini 0]; %[N�, N�_Pai, Custo]
explorado = []; %Inicia o conjunto explorado como vazio
caminho = []; %Inicia o caminho como vazio

while(~isempty(fronteira))
    %seu c�digo aqui
end
if (lenght(fronteira)==0)
        caminho = -1;
        custo = -1;
        disp('N�o foi poss�vel encontrar um caminho do n� de in�cio ao n� de destino.');
        return
end
end

'''

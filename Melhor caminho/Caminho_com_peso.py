'''' Aula Inteligencia Artificial '''
import pandas as pd
import scipy.io as sp

#Formando a tabela de distancia heuclidiana na mão
distNome = ["Arad", "Bucharest", "Craiova", "Drobeta", "Eforie", "Fagaras", "Giurgi",
        "Hirsova", "Iasi", "Lugoj", "Mehadia", "Neamt", "Oradea", "Pitesti", "Rimnicu Vilcea",
        "Sibiu", "Timisoara", "Urziceni", "Vaslui", "Zerind"];
distQuant = [366, 0, 160, 242, 161, 176, 77, 151, 226, 244, 241, 234, 380, 100, 193, 253, 329,
               80, 199, 374];

dist = pd.DataFrame(distQuant, distNome);
#=======================================================================================

explorado = []; #Inicia o conjunto explorado como vazio
caminho = []; #Inicia o caminho como vazio
fronteira = [];
custo = 0;

def estrela(mapa,ini,fim):

    G = 0
    H = getDistValue(ini)
    F = G + H 
    node = [ini, ini, G, H, F]
    custo = 0

    if(node[0] == fim):
        print('O n de inicio ja é o nó de destino.');
        return
    
    fronteira.append(node); #[Nó, NóPai, pesoCaminho, dist, soma]

    while(fronteira):
        
        node = fronteira.pop(maisBarato(fronteira)) #Nó mais leve da fronteira.
        
        explorado.append(node)  #Adiciona no  explorados o nó analisado.
        
        if( node[0] == fim):
            return solucao(ini)    
        
        tabelaPeso = mapa[mapa[node[0]]>0][node[0]]    #possiveis caminhos com respectivos pessos
        opcoes = list(tabelaPeso.index.values)         #opcoes com apenas seus nomes

        for filho in opcoes:    #Possiveis caminhos a seguir a partir do nó.
            
            G = tabelaPeso[filho];
            H = getDistValue(filho);
            F = G + H;
            filhoCompleto = [filho, node[0], G, H, F]
            
            if ( not isExplorado(filho) ):
                
                G_tempF = G + custo
                
                if( not fronteira.count(filhoCompleto) > 0 ):
                    
                    fronteira.append(filhoCompleto)
                    G_F = G_tempF
                    #F_F = G_F + H
                    #custo += F_F

                else: 
                    if( G_F > G_tempF ):
                
                        G_F = G_tempF
                        #F_F = G_F + H
                    
    if(not fronteira):
        custo = -1
        print("Não foi possível encontrar um caminho do nó de início ao nó de destino.")
        return
    return

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

def getMap():   #Gera o DataFrame do mapa para manipulação

    data = sp.loadmat('data_Romenia.mat')
    
    columname = []
    for a in data['labels']:
        columname.append(a[0][0])

    df = pd.DataFrame(data['A'],columns=columname, index=columname)

    return(df)

def getDistValue(cidade):   #Valor na tabela dist
    return dist.loc[cidade][0]

def isExplorado(filho): #Verifica se a cidade ja foi explorada
    isEx = False;
    
    for ex in explorado:
        if (ex[0] == filho):
            isEx = True;
            break;
    return isEx


def main():
    mapa = getMap()
    estrela(mapa,'Lugoj','Bucharest')

#Inicio do programa==========================================
    
main()

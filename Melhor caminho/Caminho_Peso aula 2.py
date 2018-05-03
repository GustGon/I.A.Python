'''' Aula Inteligencia Artificial '''
import pandas as pd
import scipy.io as sp


distNome = ["Arad", "Bucharest", "Craiova", "Drobeta", "Eforie", "Fagaras", "Giurgi",
        "Hirsova", "Iasi", "Lugoj", "Mehadia", "Neamt", "Oradea", "Pitesti", "Rimnicu Vilcea",
        "Sibiu", "Timisoara", "Urziceni", "Vaslui", "Zerid"]
distQuant = [366, 0, 160, 242, 161, 176, 77, 151, 226, 244, 241, 234, 380, 100, 193, 253, 329,
               80, 199, 374]

explorado = []; #Inicia o conjunto explorado como vazio
caminho = []; #Inicia o caminho como vazio
fronteira = [];

def estrela(mapa,ini,fim):

    G = 0
    H = 0
    F = G + H 
    node = [ini, G, H, F]
    custo = 0
    #dist = pd.DataFrame(distQuant, distNome)

    if(node[0] == fim):
        print('O n de inicio ja é o nó de destino.');
        return
    
    fronteira.append(node); #[Nó, Nó_Pai, Custo]

    while(fronteira):

        #ind = maisBarato(fronteira)
        node = fronteira.pop(0) #Nó mais leve da fronteira.
        if( node[0] == fim):
            return solucao(node[0], ini)
        
        explorado.append(node)  #Adiciona no  explorados o nó analisado.
        
        tabelaPeso = mapa[mapa[node[0]]>0][node[0]]    #possiveis caminhos com respectivos pessos
        opcoes = list(tabelaPeso.index.values)         #opcoes com apenas seus nomes

        for filho in opcoes:    #Possiveis caminhos a seguir a partir do nó.
            
            G = tabelaPeso[filho]
            #H_F = dist[0]
            filhoCompleto = [filho[0], node[0], filho[1]]  
            
            if ( not explorado.count(filhoCompleto) > 0 ):# or not fronteira.count(filhoCompleto) > 0 :   #TODO: Nao esta verificando direito Explorado e Fronteira
                
                G_tempF = G + custo
                
                if( not fronteira.count(filhoCompleto) > 0 ):
                    
                    fronteira.append([filho,node[0],node[2]])
                    G_F = G_tempF
                    F_F = G_F + H_F

                else:             
                    if( G_F > G_tempF ):
                    
                        G_F = G_tempF
                        F_F = G_F + H_F
                    
    if(not fronteira):
        caminho = -1
        custo = -1
        print("Não foi possível encontrar um caminho do nó de início ao nó de destino.")
        return
    return

def maisBarato(fronteira):
    
    ref = 1000000000000
    
    for front in fronteira:
        peso = front[len(front) - 1]
        if ( peso < ref ):
            maisBarato = front.index
            #maisBarato = fronteira.pop(fronteira.index)
            
    return maisBarato

def solucao(fim,ini):

    menor = []
    menor.append(explorado[len(explorado) - 1][0])
    
    proximo = explorado[len(explorado) - 1][0]
    
    for n in range(len(explorado) - 1,0,-1):
        if ( explorado[n][0] == proximo ):
            menor.append(explorado[n][1])
            proximo = explorado[n][1]
        if ( proximo == ini ):
            break
    for p in range(len(menor) - 1,-1,-1):
        caminho.append(menor[p])    
    caminho.append(fim)
        
    return print(caminho)

def getMap():

    data = sp.loadmat('data_Romenia.mat')
    
    columname = []
    for a in data['labels']:
        columname.append(a[0][0])

    df = pd.DataFrame(data['A'],columns=columname, index=columname)

    return(df)

def main():
    #mapa = getMap()
    dist = pd.DataFrame(distQuant, distNome)
    tt = dist.index("Arad")
    #estrela(mapa,'Arad','Bucharest')
    #H_F = 
    print(tt)

#Inicio do programa
    
main()

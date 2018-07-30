'''' Aula Inteligencia Artificial '''
import pandas as pd
import scipy.io as sp


#Matriz de caminhos e custos.
#Pegar pelo excel ou fazer na mao

explorado = []; #Inicia o conjunto explorado como vazio
caminho = []; #Inicia o caminho como vazio
fronteira = [];

def bfd(mapa,ini,fim):

    node = ini
    custo = 0

    if(node == fim):
        caminho = 0;
        custo = 0;
        print('O n de inicio ja é o nó de destino.');
        return
    

    fronteira.append([ini, ini, 0]); #[Nó, Nó_Pai, Custo]
    
    while(fronteira):

        node = fronteira.pop(0) #Tira da fronteira o nó analisado.
        explorado.append(node)  #Adiciona no  explorados o nó analisado.
        
        aux = mapa[mapa[node[0]]>0][node[0]]    #possiveis caminhos com respectivos pessos
        opcoes = list(aux.index.values)         #opcoes com apenas seus nomes

        for filho in opcoes:    #Possiveis caminhos a seguir a partir do nó.
            filhoCompleto = [filho, node[0], 0]  
            if not explorado.count(filhoCompleto) > 0 or not fronteira.count(filhoCompleto) > 0 :   #TODO: Nao esta verificando direito Explorado e Fronteira
                if( filho == fim ):
                    return solucao(filho,ini)
                else:
                    fronteira.append([filho,node[0],0])
        
    if(not fronteira):
        caminho = -1
        custo = -1
        print("Não foi possível encontrar um caminho do nó de início ao nó de destino.")
        return
    return

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
    mapa = getMap()
    
    bfd(mapa,'Neamt','Bucharest')


#Inicio do programa
    
main()

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:05:14 2018

@author: elcio
"""
import subprocess
import matplotlib.pyplot as plt
from pandas import pandas as pd

def normalizar (dados_normaliza,df,val):
    minimo=dados_normaliza.min()-(dados_normaliza.min()*0.1)
    maximo=dados_normaliza.max()+(dados_normaliza.max()*0.1)
    
    en = df.columns[range(0, df.shape[1],1)]
    cont=range(0, df.shape[1],1)
    for i in cont:
        df[en[i]] = (df[en[i]]-minimo[en[i]])/(maximo[en[i]]-minimo[en[i]]) 
        
    en_val = val.columns[range(0, val.shape[1],1)]
    cont=range(0, val.shape[1],1)
    for i in cont:
        val[en_val[i]]=((val[en_val[i]]-minimo[en_val[i]])/(maximo[en_val[i]]-minimo[en_val[i]]))
    
    return (minimo, maximo, df, val)    
    
    
def formatar (df, val):
    en = df.columns[range(0, df.shape[1]-1,1)]
    en_val = val.columns[range(0, df.shape[1]-1,1)]

    sa=df.columns[df.shape[1]-1]
    sa_val=df.columns[val.shape[1]-1]

    entrada = pd.DataFrame(df,columns=en)
    saida=pd.DataFrame(df,columns=[sa])

    entrada_val = pd.DataFrame(val,columns=en_val)
    saida_val=pd.DataFrame(val,columns=[sa_val])

    entrada = entrada.transpose()
    saida = saida.transpose()

    entrada_val = entrada_val.transpose()
    saida_val = saida_val.transpose()

    ent=entrada.shape
    ent_val=entrada_val.shape

    sai=saida.shape
    sai_val=saida.shape

    entrada = entrada.to_string(index=False, header=False)
    saida = saida.to_string(index=False, header=False)

    entrada_val = entrada_val.to_string(index=False, header=False)
    saida_val = saida_val.to_string(index=False, header=False)
    
    f = open("x.txt", "w")
    f.write(entrada)
    f.close()

    f = open("yd.txt", "w")
    f.write(saida)
    f.close()

    f = open("x_valid.txt", "w")
    f.write(entrada_val)
    f.close()

    f = open("yd_valid.txt", "w")
    f.write(saida_val)
    f.close()

    return (ent, ent_val, sai, sai_val)


def treinar(ent, ent_val, sai, sai_val):
 
 
    while True:
        neuro=input('Entre com quantidade de neurônios (Por exemplo, 2): ')
        taxa=input('Entre com a taxa de aprendizado (Por exemplo, 0.1): ')
        ed=input('Entre com o erro desejado (Por exemplo, 0.01): ')
        epoca=input('Entre com numero máximo de epocas (Por exemplo, 10000): ')
        entrada_treina = pd.DataFrame({'a': [ent[1], ent_val[1], ent[0],sai[0],neuro,taxa,ed,epoca]})
        entrada_treina = entrada_treina.to_string(index=False, header=False)
        f = open("entrada.txt", "w")
        f.write(entrada_treina)
        f.close()
        p = subprocess.Popen('treina_bp_gen_ss.exe')
        p.wait()
        erro_gen=pd.read_csv('erro_gen_menor.txt', sep="\s+", header=None)
        erro=pd.read_csv('erro.txt', sep="\s+", header=None)
        orig = plt.plot(erro, color='blue',label='Treinamento')
        e_min = plt.plot(erro_gen, color='red', label='Validação')
        plt.legend(loc='best')
        plt.title('Treinamento e validação')
        plt.show(block=False)
        erro_gen=pd.read_csv('erro_gen_menor.txt', sep="\s+", header=None)
        erro_minimo=erro_gen.min()
        
        erro_m = erro_minimo.to_string(index=False, header=False)
        print("\n Erro Quadrático =  %s " % (erro_m))

        opc=input('\n \n \n Deseja treinar mais configuração (s/n)? ')

        if opc=='n':
            break  
            return (neuro)
      
def treina_melhor(ent, ent_val, sai, sai_val):
    
    neuro=input('Entre com quantidade de neurônios (Por exemplo, 2): ')
    taxa=input('Entre com a taxa de aprendizado (Por exemplo, 0.1): ')
    ed=input('Entre com o erro desejado (Por exemplo, 0.01): ')
    epoca=input('Entre com numero máximo de epocas (Por exemplo, 10000): ')
    entrada_treina = pd.DataFrame({'a': [ent[1], ent_val[1], ent[0],sai[0],neuro,taxa,ed,epoca]})
    entrada_treina = entrada_treina.to_string(index=False, header=False)
    f = open("entrada.txt", "w")
    f.write(entrada_treina)
    f.close()
    p = subprocess.Popen('treina_bp_gen_ss.exe')
    p.wait()
    erro_gen=pd.read_csv('erro_gen_menor.txt', sep="\s+", header=None)
    erro=pd.read_csv('erro.txt', sep="\s+", header=None)
    orig = plt.plot(erro, color='blue',label='Treinamento')
    e_min = plt.plot(erro_gen, color='red', label='Validação')
    plt.legend(loc='best')
    plt.title('Treinamento e validação')
    plt.show(block=False)
    erro_gen=pd.read_csv('erro_gen_menor.txt', sep="\s+", header=None)
    erro_minimo=erro_gen.min()
    erro_m = erro_minimo.to_string(index=False, header=False)
    print("\n Erro Quadrático =  %s " % (erro_m))
    
 #   print('O erro minimo é: ', erro_minimo) 
    
    return (neuro)
      
def normalizar_ativa (avalia,minimo,maximo):      
    en_aval = avalia.columns[range(0, avalia.shape[1],1)]
    cont=range(0, avalia.shape[1],1)
    for i in cont:
        avalia[en_aval[i]] = (avalia[en_aval[i]]-minimo[en_aval[i]])/(maximo[en_aval[i]]-minimo[en_aval[i]])
    return (avalia)       
      

def formatar_ativa (avalia):
     en_aval = avalia.columns[range(0, avalia.shape[1]-1,1)]
     sa_aval = avalia.columns[avalia.shape[1]-1]
     
     entrada_avalia = pd.DataFrame(avalia,columns=en_aval)
     saida_avalia=pd.DataFrame(avalia,columns=[sa_aval])      
     
     entrada_avalia = entrada_avalia.transpose()
     saida_avalia = saida_avalia.transpose()
     
     ent_avalia=entrada_avalia.shape
     sai_avalia=saida_avalia.shape
     
     entrada_avalia = entrada_avalia.to_string(index=False, header=False)
     saida_avalia = saida_avalia.to_string(index=False, header=False)
     
     f = open("x_gen.txt", "w")
     f.write(entrada_avalia)
     f.close()
     
     f = open("yd_gen.txt", "w")
     f.write(saida_avalia)
     f.close()
     
     return (ent_avalia, sai_avalia)
 
    
def ativa (avalia, ent_avalia, sai_avalia, neuro, minimo, maximo):
    entrada_ativa = pd.DataFrame({'a': [ent_avalia[1],ent_avalia[0],sai_avalia[0] ,neuro]})
    entrada_ativa = entrada_ativa.to_string(index=False, header=False)
    f = open("entrada_ativa.txt", "w")
    f.write(entrada_ativa)
    f.close()
    p = subprocess.Popen('ativa_bp_gen_ss')
    p.wait()    
    y2=pd.read_csv('y2.txt', sep="\s+", header=None)
    #y2 = (y2*(maximo['Valor']-minimo['Valor']))+minimo['Valor']
    en1 = avalia.columns[avalia.shape[1]-1]
    y2 = (y2*(maximo[en1]-minimo[en1]))+minimo[en1]
    return (y2)
    
def apresenta (y2,saida_real):
    saida_rna=y2.transpose()
    import numpy as np
    ss_rna=np.array(saida_rna)
    ss_real=np.array(saida_real)
    dif=ss_real-ss_rna
    ss_real_pt = plt.plot(ss_real, 'ro', color='blue',label='Valor Real')
    ss_rna_pt = plt.plot(ss_rna, 'b*', color='green', label='VAlor Rede Neural')
    plt.legend(loc='best')
    plt.show(block=False)
    saida_p = saida_rna.to_string(index=False, header=False)
    saida_r = saida_real.to_string(index=False, header=False)

    cont=range(0, saida_rna.shape[1],1)

    for i in cont:
        saida_p = saida_rna.to_string(index=False, header=False)
        print("\n Valor ofertado = \n %s " % (saida_r))


    for i in cont:
        saida_p = saida_rna.to_string(index=False, header=False)
        print("\n Estimação da Rede Neural Artificial = \n %s " % (saida_p))
    
    
    




    
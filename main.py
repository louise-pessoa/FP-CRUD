import os

historico_geral = []

def adicionar_no_arquivo(movimentos, data, tempo, tipo, cont_arquivos):
    with open(f"treino-crossfit{cont_arquivos+1}.txt", "w", encoding='utf8') as historico:
        movimentos_lista = [movimentos.capitalize() for movimentos in movimentos.split(", ")]

        historico.write("Data: " + data + "\nDuração: " + tempo + " minutos\nTipo de treino: " + tipo)
        historico.write("\nMovimentos: \n")

        for i in range(len(movimentos_lista)) :
            historico.write(str(i+1) + ". " + movimentos_lista[i] + "\n")
            
def lista_arquivos(comeco, fim, caminho):
    historico_treinos = []
    for arquivo in os.listdir(caminho):
        if arquivo.startswith(comeco) and arquivo.endswith(fim):
            historico_treinos.append(arquivo)
            historico_treinos.reverse()

    return historico_treinos
cont_arquivos = len(lista_arquivos("treino-crossfit", ".txt", "."))

def ler_arquivos(historico_geral):
    if historico_geral == []:
        print("Nenhum treino encontrado.")
        return
    for treino in historico_geral:
        try:
            with open(treino, "r", encoding="utf-8") as arquivo_treino:
                print(f"\nArquivo: {treino}")
                print(arquivo_treino.read())
                print("/\\" * 15)
        except Exception as e:
            print(f"Erro ao ler o arquivo {treino}: {e}")

while True:
    historico = f"treino-crossfit{cont_arquivos}.txt"
    opcoes_usuario = int(input("\nEscolha uma ação:\n1-CREATE\n2-READ\n3-UPDATE\n4-DELETE\nDigite apenas o número correspondente à ação: "))
    
    try:
        #inputs para adicionar
        if opcoes_usuario == 1:
            data = input("Data do treino (exemplo: xx/xx/xxxx): ")
            tempo = input("Tempo de duração do treino em minutos: ")
            tipo = input("Tipo do treino (AMRAP, EMOM, For Time): ")
            movimentos = input("Movimentos (separe os movimentos por vírgulas): ")
            lista_arquivos("treino-crossfit", ".txt", ".")
            adicionar_no_arquivo(movimentos, data, tempo, tipo, cont_arquivos)
            #print(f"Treino salvo em: treino-crossfit{cont_arquivos+1}.txt")
            historico_geral = lista_arquivos("treino-crossfit", ".txt", ".")
            

#READ
        elif opcoes_usuario == 2:
            #chamando função de leitura
            ler_arquivos(lista_arquivos)


#UPDATE


#DELETE

    #encerrar o código
    except Exception as e:
        print(f"Erro: {e}")
        break
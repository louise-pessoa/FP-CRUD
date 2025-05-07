import os

lista_seila = []
cont_arquivos = 0

def adicionar_no_arquivo(movimentos, data, tempo, tipo, cont_arquivos):
    with open(f"treinos-crossfit{cont_arquivos}.txt", "w", encoding='utf8') as historico:
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
cont_arquivos = len(lista_arquivos("treinos-crossfit", ".txt", "."))


def ler_arquivos(historico_treinos):
    if not historico_treinos:
        print("Nenhum treino encontrado.")
        return
    for treino in historico_treinos:
        try:
            with open(treino, "r", encoding="utf-8") as arquivo_treino:
                print(f"\nArquivo: {treino}")
                print(arquivo_treino.read())
                print("-" * 10)
        except Exception as e:
            print(f"Erro ao ler o arquivo {treino}: {e}")

while True:
    cont_arquivos += 1
    historico = f"treinos-crossfit{cont_arquivos}.txt"
    opcoes_usuario = int(input("Escolha uma ação:\n1-CREATE\n2-READ\n3-UPDATE\n4-DELETE\nDigite apenas o número correspondente à ação: "))
    
    #inputs para adicionar
    if opcoes_usuario == 1:
        data = input("Data do treino (exemplo: xx/xx/xxxx): ")
        tempo = input("Tempo de duração do treino em minutos: ")
        tipo = input("Tipo do treino (AMRAP, EMOM, For Time) : ")
        movimentos = input("Movimentos (separe os movimentos por vígulas): ")
        adicionar_no_arquivo(movimentos, data, tempo, tipo, cont_arquivos)
        print(f"Treino salvo em: treinos-crossfit{cont_arquivos}.txt")
        lista_arquivos("treinos-crossfit", ".txt", ".")
            

#READ
    elif opcoes_usuario == 2:
        if lista_seila == []:
            print("O histórico está vazio, não há o que mostrar.")
        else:
            #chamando função de leitura
            ler_arquivos(lista_seila)


#UPDATE
    elif opcoes_usuario == 3:
        indice = int(input("Digite o índice (a partir de 0) do elemento a ser atualizado: "))
        if indice in range (len(lista_seila)):
            lista_seila[indice] = input("Digite o novo elemento: ")
            i=0
            for i in range (len(lista_seila)):
                print(i,"-",lista_seila[i])
        else:
            print("Este índice não é válido!")


#DELETE
    elif opcoes_usuario == 4:
        indice = int(input("Digite o índice (a partir de 0) do elemento a ser excluído: "))
        if indice in range(len(lista_seila)):
            elementoRemovido = lista_seila.pop(indice)
            print(elementoRemovido, "foi removido da lista")
            if lista_seila == []:
                print("Lista atualizada: ")
            else:
                i=0
                print("Lista atualizada:")
                for i in range (len(lista_seila)):
                    print(f"{i}- {lista_seila[i]}")
        else:
            print("Este índice não é válido!")


#encerrar o código
    else:
        print("Opção inválida, o programa será encerrado!")
        break

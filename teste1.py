historico_treinos = []

while True:
    opcoes_usuario = int(input("Escolha uma ação:\n1-CREATE\n2-READ\n3-UPDATE\n4-DELETE\nDigite apenas o número correspondente à ação: "))

#CREATE
    if opcoes_usuario == 1:
        data = (input("Data do treino (exemplo: xx xx xxxx): "))
        historico_treinos[data] = (input("Adicionar treino: "))
        data = input("")
        for value in (historico_treinos):
            print(value)

#READ
    elif opcoes_usuario == 2:
        if historico_treinos == []:
            print("A lista está vazia, não há o que mostrar.")
        else:
            with open("treinos-crossfit.txt","r", encoding="utf8") as historico:
                ler_historico = historico.read()
                print(ler_historico)

#UPDATE
    elif opcoes_usuario == 3:
        indice = int(input("Digite o índice (a partir de 0) do elemento a ser atualizado: "))
        if indice in range (len(historico_treinos)):
            historico_treinos[indice] = input("Digite o novo elemento: ")
            i=0
            for i in range (len(historico_treinos)):
                print(i,"-",historico_treinos[i])
        else:
            print("Este índice não é válido!")

#DELETE
    elif opcoes_usuario == 4:
        indice = int(input("Digite o índice (a partir de 0) do elemento a ser excluído: "))
        if indice in range(len(historico_treinos)):
            elementoRemovido = historico_treinos.pop(indice)
            print(elementoRemovido, "foi removido da lista")
            if historico_treinos == []:
                print("Lista atualizada: ")
            else:
                i=0
                print("Lista atualizada:")
                for i in range (len(historico_treinos)):
                    print(f"{i}- {historico_treinos[i]}")
        else:
            print("Este índice não é válido!")

#encerrar o código
    else:
        print("Opção inválida, o programa será encerrado!")
        break
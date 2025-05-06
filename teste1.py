dicionario_treinos = {}

while True:
    opcoesUsuario = int(input("Escolha uma ação:\n1-CREATE\n2-READ\n3-UPDATE\n4-DELETE\nDigite apenas o número correspondente à ação: "))

#CREATE
    if opcoesUsuario == 1:
        dicionario_treinos(input("Adicionar treino: "))
        data = input("")
        for value in (dicionario_treinos):
            print(value)

#READ
    elif opcoesUsuario == 2:
        if dicionario_treinos == {}:
            print("O histórico está vazio, não há o que mostrar.")
        # else:
        #     arquivo

#UPDATE
    elif opcoesUsuario == 3:
        indice = int(input("Digite o índice (a partir de 0) do elemento a ser atualizado: "))
        if indice in range (len(dicionario_treinos)):
            dicionario_treinos[indice] = input("Digite o novo elemento: ")
            i=0
            for i in range (len(dicionario_treinos)):
                print(i,"-",dicionario_treinos[i])
        else:
            print("Este índice não é válido!")

#DELETE
    elif opcoesUsuario == 4:
        indice = int(input("Digite o índice (a partir de 0) do elemento a ser excluído: "))
        if indice in range(len(dicionario_treinos)):
            elementoRemovido = dicionario_treinos.pop(indice)
            print(elementoRemovido, "foi removido da lista")
            if dicionario_treinos == []:
                print("Lista atualizada: ")
            else:
                i=0
                print("Lista atualizada:")
                for i in range (len(dicionario_treinos)):
                    print(f"{i}- {dicionario_treinos[i]}")
        else:
            print("Este índice não é válido!")

#encerrar o código
    else:
        print("Opção inválida, o programa será encerrado!")
        break
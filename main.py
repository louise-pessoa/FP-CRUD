import os

historico_geral = []

def adicionar_no_arquivo(movimentos, data, tempo, tipo, data_conteudo):
        with open(f"treino-crossfit{data}.txt", "w", encoding='utf8') as arquivo:
            movimentos_lista = [movimentos.capitalize() for movimentos in movimentos.split(", ")]
            arquivo.write("Data: " + data_conteudo + "\nDuração: " + tempo + " minutos\nTipo de treino: " + tipo)
            arquivo.write("\nMovimentos: \n")

            for i in range(len(movimentos_lista)):
                arquivo.write(str(i+1) + ". " + movimentos_lista[i] + "\n")
            
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
            with open(treino, "r", encoding="utf-8") as nome_arquivo:
                print(f"\nArquivo: {treino}")
                print(nome_arquivo.read())
        except Exception as e:
            print(f"Erro ao ler o arquivo {treino}: {e}")

def ler_arquivo(arquivo_p_ler):
    if not arquivo_p_ler:
        print("Nenhum treino encontrado.")
        return
    try:
        with open(arquivo_p_ler, "r", encoding="utf-8") as nome_arquivo:
            print(f"\nArquivo: {arquivo_p_ler}")
            print(nome_arquivo.read())
            print("/\\" * 15)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

#FILTRAR
def filtragem():
    return

def editar_arquivo(arquivo_p_editar, opcao_edicao, edicao):
    for i in arquivo_p_editar:
        if opcao_edicao == 1 and i == 0:
            arquivo_p_editar[i] = "Data: "+edicao
            
        elif opcao_edicao == 2 and i == 1:
            arquivo_p_editar[i] = "Tempo de duração: "+edicao+" minutos"
            
        elif opcao_edicao == 3 and i == 2:
            arquivo_p_editar[i] = "Tipo de treino: "+edicao

        linha_editada = arquivo_p_editar
    return linha_editada

def editar_movim_arquivo(arquivo_p_editar, edicao):
    edicao = [edicao.capitalize() for movimento in edicao.split(", ")]
    for i in arquivo_p_editar:
        if i == 3:
            for j in range(len(edicao)):
                arquivo_p_editar[j+3] = str(j+1)+". "+edicao[j]+"\n"
    movimentos_editados = arquivo_p_editar
    return movimentos_editados


while True:
    
    try:
#CRIAR
        print("/\\" * 15)
        opcoes_usuario = int(input("""\nEscolha uma ação:\n1-Adicionar\n2-Visualizar\n3-Editar\n4-Deletar\n
Digite apenas o número correspondente à ação: """))
        #inputs para adicionar
        if opcoes_usuario == 1:
            print("\n"+"-"*5+"MODO DE ADIÇÃO"+"-"*5)

            data = input("Data do treino (exemplo: xx xx xxxx): ")
            data_split = data.split()
            data_nome_arquivo = "".join(data_split)
            data_conteudo = "/".join(data_split)
            nome_arquivo = f"treino-crossfit{data_nome_arquivo}.txt"
            tempo = input("Tempo de duração do treino em minutos: ")
            tipo = input("Tipo do treino (AMRAP, EMOM, For Time): ")
            movimentos = input("Movimentos (separe os movimentos por ','): ")
            lista_arquivos("treino-crossfit", ".txt", ".")
            adicionar_no_arquivo(movimentos, data_nome_arquivo, tempo, tipo, data_conteudo)
            
            print(f"Treino salvo em: treino-crossfit{data_nome_arquivo}.txt")
            historico_geral = lista_arquivos("treino-crossfit", ".txt", ".")
            

#LER
        elif opcoes_usuario == 2:
            try:
                print("\n"+"-"*5+"MODO DE VISUALIZAÇÃO"+"-"*5)
                filtro_ler = int(input("""1- Todo o histórico;
2- Por nome do arquivo;
3- Por tipo de treino;
4- Por movimento.
Digite a opção a ser visualizada: """))
                if filtro_ler == 1:
                #chamando função de leitura
                    ler_arquivos(lista_arquivos("treino-crossfit", ".txt", "."))
                elif filtro_ler == 2:
                    print("\n"+"-"*5+"MODO DE SELEÇÃO"+"-"*5)
                    arquivo_por_linha = '\n'.join(historico_geral)
                    print(f"Escolha um dos arquivos abaixo para visualizar:\n{arquivo_por_linha}")
                    arquivo_p_ler = input("Digite (ou copie e cole) o nome do arquivo a ser visualizado:\n")
                    if not arquivo_p_ler:
                        print("Treino não encontrado.")
                    else:
                        ler_arquivo(arquivo_p_ler)
                #elif filtro_ler == 3:
                    #inserir funcao de filtro
                #elif filtro_ler == 4:
                    #inserir funcao de filtro
                else:
                    print("Opção inválida")
            except Exception as e:
                print(f"Erro: {e}")
                break


#SELECIONAR
        elif opcoes_usuario == 3:
            try:
                print("\n"+"-"*5+"MODO DE SELEÇÃO"+"-"*5)
                arquivo_por_linha = '\n'.join(historico_geral)
                print(f"Escolha um dos arquivos abaixo para editar:\n{arquivo_por_linha}")
                arquivo_p_editar = input("Digite (ou copie e cole) o nome do arquivo a ser editado:\n")
#EDITAR
                print("\n"+"-"*5+"MODO DE EDIÇÃO"+"-"*5)
                opcao_edicao = int(input("""1- Data (xx xx xxxx);\n2- Tempo de duração (minutos);\n3- Tipo de treino;\n4- Movimentos (separados por ", ").
Digite a opção a ser editada: """))
                
                edicao = input("Digite o elemento certo: ")

                if opcao_edicao == 1:
                    edicao_split = edicao.split()
                    edicao_conteudo = "/".join(edicao_split)
                    arquivo_editado = editar_arquivo(arquivo_p_editar, opcao_edicao, edicao_conteudo)
                    historico_geral[arquivo_p_editar] = arquivo_editado

                    #mudar data no nome do arquivo
                    edicao_nome = "".join(edicao_split)
                    os.rename(arquivo_p_editar, f'treino-crossfit{edicao_nome}.txt')
                    print(historico_geral)
                    historico_geral.sort()

                elif opcao_edicao == 2 or opcao_edicao == 3:
                    editar_arquivo(arquivo_p_editar, opcao_edicao, edicao)

                elif opcao_edicao == 4:
                    editar_movim_arquivo(arquivo_p_editar, edicao)

                else:
                    print("Opção inválida")

            except Exception as e:
                print(f"Erro: {e}")
                break

#SELECIONAR
        elif opcoes_usuario == 3:
                print("\n"+"-"*5+"MODO DE SELEÇÃO"+"-"*5)
                arquivo_por_linha = '\n'.join(historico_geral)
                print(f"Escolha um dos arquivos abaixo para deletar:\n{arquivo_por_linha}")
                arquivo_p_remover = input("Digite (ou copie e cole) o nome do arquivo a ser removido:\n")
#DELETAR
                print("\n"+"-"*5+"MODO DE REMOÇÃO"+"-"*5)

#ENCERRAR
    except ValueError as e:
        print(f"Erro: {e}")
        break
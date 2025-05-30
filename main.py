import os
import random
os.system('cls')
historico_geral = []
metas = []
metas_concluidas = []

def adicionar_no_arquivo(movimentos, data, tempo, tipo, data_conteudo):
        with open(f"treino-crossfit{data}.txt", "w", encoding='utf8') as arquivo:
            movimentos_lista = [movimentos.capitalize() for movimentos in movimentos.split(", ")]
            arquivo.write("Data: " + data_conteudo + "\nDuração: " + tempo + " minutos\nTipo de treino: " + tipo)
            arquivo.write("\nMovimentos:\n")

            for i in range(len(movimentos_lista)):
                arquivo.write(str(i+1) + ". " + movimentos_lista[i] + "\n")
            
def lista_arquivos(comeco, fim, caminho):
    historico_treinos = []
    for arquivo in os.listdir(caminho):
        if arquivo.startswith(comeco) and arquivo.endswith(fim):
            historico_treinos.append(arquivo)

    i = 0
    while i < len(historico_treinos):
        if historico_treinos[i] not in os.listdir(caminho):
            historico_treinos.pop(i)
        else:
            i += 1

    return historico_treinos

def carregar_historico():
    return lista_arquivos("treino-crossfit", ".txt", ".")

def inicio():
    print("="*40)
    print("SEJA BEM-VINDO AO WOD TRACKER!")
    print("Carregando treinos salvos...\n")
    return carregar_historico()
historico_geral = inicio()

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
def filtrar_treinos():
    os.system("cls")
    print("------------------ | FILTRAR TREINOS | -------------------")
    
    tipoFiltro = input("Filtrar por tipo: ").strip().lower()
    movimentoFiltro = input("Filtrar por movimento: ").strip().lower()
    dataFiltro = input("Filtrar por data: ").strip()

    treinos = []
    
    for nome_arquivo in os.listdir():
        if nome_arquivo.startswith("treino-crossfit") and nome_arquivo.endswith(".txt"):
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()
                treino = {"movimentos": []}
                lendo_movimentos = False

                for linha in linhas:
                    linha = linha.strip()
                    if linha.startswith("Data:"):
                        treino["data"] = linha[5:].strip()
                        lendo_movimentos = False
                    elif linha.startswith("Tipo de treino:"):
                        treino["tipo"] = linha[16:].strip().lower()
                        lendo_movimentos = False
                    elif linha.startswith("Movimentos:"):
                        treino["movimentos"] = []
                        lendo_movimentos = True
                    elif lendo_movimentos:
                        if linha and linha[0].isdigit() and "." in linha:
                            movimento = linha.split(". ", 1)[-1].strip().lower()
                            treino["movimentos"].append(movimento)
                        else:
                            lendo_movimentos = False

                if treino:
                    treinos.append(treino)

    resultados = []
    for t in treinos:
        tipo_ok = tipoFiltro in t.get("tipo", "") if tipoFiltro else True
        movimento_ok = any(movimentoFiltro in m for m in t.get("movimentos", [])) if movimentoFiltro else True
        data_ok = dataFiltro == t.get("data", "") if dataFiltro else True

        if tipo_ok and movimento_ok and data_ok:
            resultados.append(t)

    if resultados:
        print("\n----------------- | RESULTADOS ENCONTRADOS | -------------------")
        for t in resultados:
            print(f"Data: {t.get('data', '')}")
            print(f"Tipo: {t.get('tipo', '')}")
            print(f"Movimentos: {', '.join(t.get('movimentos', []))}")
            print("-------------------------------------------------")
    else:
        print("\nOpss... Nenhum treino encontrado :()")

    input("\nSe quiser continuar pressione o Enter... :)")

def editar_arquivo(arquivo_p_editar, opcao_edicao, edicao):
    with open(arquivo_p_editar, "r", encoding="utf8") as arquivo:
        linhas = arquivo.readlines()
    
    for i in arquivo_p_editar:
        if opcao_edicao == 1 and i == 0:
            linhas[i] = "Data: "+edicao
            
        elif opcao_edicao == 2 and i == 1:
            linhas[i] = "Tempo de duração: "+edicao+" minutos"
            
        elif opcao_edicao == 3 and i == 2:
            linhas[i] = "Tipo de treino: "+edicao

    with open(arquivo_p_editar, "w", encoding="utf8") as arquivo:
        arquivo.writelines(linhas)

    return arquivo_p_editar

def editar_movim_arquivo(arquivo_p_editar, edicao):
    edicao_lista = [e.capitalize() for e in edicao.split(", ")]

    with open(arquivo_p_editar, "r", encoding="utf8") as arquivo:
        linhas = arquivo.readlines()

    for i in range(len(linhas)):
        if linhas[i].strip() == "Movimentos:":
            for j in range(len(edicao_lista)):
                linhas[i+1+j] = f"{j+1}. {edicao_lista[j]}\n"
            
            # Apagar movimentos se a lista de edições for menor
            if len(edicao_lista) < (len(linhas) - (i+1)):
                linhas = linhas[: i+1+len(edicao_lista)]

            break

    with open(arquivo_p_editar, "w", encoding="utf8") as arquivo:
        arquivo.writelines(linhas)

    return arquivo_p_editar

def deletar_arquivo(arquivo_escolhido):
    try:
        if os.path.exists(arquivo_escolhido):
            os.remove(arquivo_escolhido)
            print(f"Arquivo {arquivo_escolhido} removido com sucesso.")
    except FileNotFoundError:
        print(f"O arquivo {arquivo_escolhido} não existe. Digite um presente na lista anterior.")

def escolha_playlists(playlists):
    playlist_feliz = [
                "1-Happy - Pharrell Williams", 
                "2-You Belong With Me - Taylor Swift", 
                "3-Camisa 10 - Turma do Pagode", 
                "4-Wannabe - Spice Girls", 
                "5-What Makes you Beautiful - One Direction",
                "6-Baby - Justin Bieber",
                "7-Last Friday Night (T.G.A.F) - Katy Perry",
                "8-FANCY - TWICE",
                "9-Ta Vendo Aquela Lua - Exaltasamba",
                "10-Dance The Night - Dua Lipa"]
    playlist_triste = [
                "1-my tears ricochet - Taylor Swift",
                "2-Hoje Sou Eu Que Não Mais Te Quero - Charlie Brown Jr.",
                "3-You're Losing Me (From The Vault) - Taylor Swift",
                "4-Roses - JAEHYUN",
                "5-illicit affairs - Taylor Swift",
                "6-Daddy Issues - The Neighbourhood",
                "7-Dealer - Lana Del Rey",
                "8-I Know it's Over - The Smiths",
                "9-Your Best American Girls - Mitski",
                "10-Bags - Clairo"]
    playlist_dangerousWoman = [
                "1-Look What You Made Me Do - Taylor Swift",
                "2-Get him back - Olivia Rodrigo!",
                "3-Dangerous Woman - Ariana Grande",
                "4-Gimme More - Britney Spears",
                "5-Breakin' Dishes - Rihanna",
                "6-Sorry Not Sorry - Demi Lovato",
                "7-Blank Space - Taylor Swift",
                "8-Popular - The Weeknd, Playboi Carti e Madonna",
                "9-Pretty Savage - BLACKPINK",
                "10-Brooklyn Baby - Lana Del Rey"]
    playlist_GOAT = [
                "1-FE!N - Travis Scott e Playboi Carti",
                "2-The Real Slim Shady - Eminem",
                "3-Creppin - Metro Boomin, The Weeknd e 21 Savage",
                "4-Come Around Me - Justin Bieber",
                "5-In My Room - Frank Ocean",
                "6-HUMBLE. - Kendrick Lamar",
                "7-Pyramids - Frank Ocean",
                "8-Les - Childish Gambino",
                "9-Mask Off - Future",
                "10-New Drop - Don Toliver"]
    playlist_cbj = [
                "1-Céu Azul",
                "2-Dona Do Meu Pensamento",
                "3-Só Por Uma Noite",
                "4-Dias De Luta Dia De Glória",
                "5-Só Os Loucos Sabem",
                "6-Zóio De Lula",
                "7-Lugar Ao Sol",
                "8-O Errado Que Deu Certo",
                "9-Proibida Pra Mim(Grazon)",
                "10-Ela Vai Voltar (Todos Os Defeitos De Uma Mulher Perfeita)"]
    playlist_taylor = [
                "1-Picture To Burn",
                "2-The Way I Loved You",
                "3-The Story Of Us",
                "4-Babe",
                "5-Is It Over Now",
                "6-I Did Something Bad",
                "7-The Man",
                "8-august",
                "9-no body no crime",
                "10-Bejeweled",
                "11-But Daddy I Love Him"]
    
    if playlists == 1:
      for playlist in playlist_feliz:
        print(playlist)
    elif playlists == 2:
      for playlist in playlist_triste:
        print(playlist)
    elif playlists == 3:
      for playlist in playlist_dangerousWoman:
        print(playlist)
    elif playlists == 4:
      for playlist in playlist_GOAT:
        print(playlist)
    elif playlists == 5:
      for playlist in playlist_cbj:
        print(playlist)
    elif playlists == 6:
      for playlist in playlist_taylor:
        print(playlist)
    else:
        print("Essa playlist não existe.")

    return print

def extrair_movimentos():
    movimentos_totais = set()
    arquivos = lista_arquivos("treino-crossfit", ".txt", ".")
    for nome_arquivo in arquivos:
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                lendo_movimentos = False
                for linha in arquivo:
                    linha = linha.strip().lower()
                    if "movimentos:" in linha:
                        lendo_movimentos = True
                    elif lendo_movimentos and linha and linha[0].isdigit() and "." in linha:
                        movimento = linha.split(". ", 1)[-1]
                        movimentos_totais.add(movimento)
                    elif lendo_movimentos and not linha:
                        lendo_movimentos = False
        except Exception as e:
            print(f"Erro ao extrair movimentos de {nome_arquivo}: {e}")
    return list(movimentos_totais)


def sugerir_wod():
    print("\n"+"-"*5+"SUGESTÃO ALEATÓRIA DE WOD"+"-"*5)
   
    movimentos_disponiveis = extrair_movimentos()
    if not movimentos_disponiveis:
        print("Nenhum movimento encontrado no histórico! Adicione treinos antes de usar essa função.")
        input("Pressione Enter para continuar...")
        return


    tipos_wod = ["AMRAP", "EMOM", "For Time"]
    tipo_aleatorio = random.choice(tipos_wod)
    duracao_aleatoria = random.randint(10, 40)
    num_movimentos = random.randint(2, min(5, len(movimentos_disponiveis)))
    movimentos_aleatorios = random.sample(movimentos_disponiveis, num_movimentos)


    print(f"\nTipo de treino: {tipo_aleatorio}")
    print(f"Duração: {duracao_aleatoria} minutos")
    print("Movimentos sugeridos:")
    for mov in movimentos_aleatorios:
        print(f"- {mov}")
   
    input("\nPressione Enter para continuar")


while True:
    try:
#CRIAR
        print("/\\" * 15)
        opcoes_usuario = int(input("""\nEscolha uma ação:\n1- Adicionar\n2- Visualizar
3- Editar\n4- Deletar\n5- Suas metas\n6- Sua playlist\n7- Sugerir um Wod aleatório
Digite apenas o número correspondente à ação: """))
        #inputs para adicionar
        if opcoes_usuario == 1:
            print("\n"+"-"*5+"MODO DE ADIÇÃO"+"-"*5)

            data = input("Data do treino (exemplo: xx xx xxxx): ")

            data_split = data.split()
            data_nome_arquivo = "".join(data_split)
            data_conteudo = "/".join(data_split)
            
            tempo = input("Tempo de duração do treino em minutos: ")
            tipo = input("Tipo do treino (AMRAP, EMOM, For Time): ")
            movimentos = input("""Movimentos (separe os movimentos por ", "): """)
            
            lista_arquivos("treino-crossfit", ".txt", ".")
            adicionar_no_arquivo(movimentos, data_nome_arquivo, tempo, tipo, data_conteudo)
            
            print(f"\nTreino salvo como: treino-crossfit{data_nome_arquivo}.txt")
            historico_geral = lista_arquivos("treino-crossfit", ".txt", ".")

#LER
        elif opcoes_usuario == 2:
            print("\n"+"-"*5+"MODO DE VISUALIZAÇÃO"+"-"*5)
            filtro_ler = int(input("""Filtrar arquivos:\n1- Todo o histórico;
2- Por nome do arquivo;
3- Por tipo de treino;
4- Por movimento.
Digite a opção de filtro: """))
            if filtro_ler == 1:
                ler_arquivos(historico_geral)
            elif filtro_ler == 2:
                if not historico_geral:
                    print ("Nenhum treino encontrado :( )")
                else: 
                    print("\n Arquivos disponíveis: ")
                for i, arquivo in enumerate(historico_geral): 
                    print (f"{i+1}.{arquivo}")
                try:
                    escolha = int(input("Escolha o número do arquivo que deseja visualizar: "))
                    if 1<= escolha <= len(historico_geral):
                        ler_arquivo(historico_geral[escolha-1])
                    else:
                        print ("Opss... Número Inválido :/")
                except ValueError:
                    print ("Entrada Inválida :/")
            elif filtro_ler == 3:
                filtrar_treinos()
            elif filtro_ler == 4: 
                filtrar_treinos()
            else:
                print ("Opção de filtragem inválida...")               

#SELECIONAR
        elif opcoes_usuario == 3:
            print("\n"+"-"*5+"MODO DE SELEÇÃO"+"-"*5)
            arquivo_por_linha = '\n'.join(historico_geral)
            print(f"Escolha um dos arquivos abaixo para editar:\n{arquivo_por_linha}")
            arquivo_p_editar = input("Digite (ou copie e cole) o nome do arquivo a ser editado:\n")
#EDITAR
            print("\n"+"-"*5+"MODO DE EDIÇÃO"+"-"*5)
            opcao_edicao = int(input("""1- Data (xx xx xxxx);\n2- Tempo de duração (minutos);\n3- Tipo de treino;
4- Movimentos (separados por ", ").
Digite a opção a ser editada: """))
                
            edicao = input("Digite o elemento certo: ")

            if opcao_edicao == 1:
                #data no CONTEÚDO
                edicao_split = edicao.split()
                edicao_conteudo = "/".join(edicao_split)
                arquivo_p_editar = editar_arquivo(arquivo_p_editar, opcao_edicao, edicao_conteudo)

                #data no NOME
                edicao_nome = "".join(edicao_split)
                os.rename(arquivo_p_editar, f'treino-crossfit{edicao_nome}.txt')


            elif opcao_edicao == 2 or opcao_edicao == 3:
                arquivo_p_editar = editar_arquivo(arquivo_p_editar, opcao_edicao, edicao)

            elif opcao_edicao == 4:
                arquivo_p_editar = editar_movim_arquivo(arquivo_p_editar, edicao)

            else:
                print("Opção inválida")

#SELECIONAR
        elif opcoes_usuario == 4:
                print("\n"+"-"*5+"MODO DE REMOÇÃO"+"-"*5)
                arquivo_por_linha = '\n'.join(historico_geral)
                print(f"Escolha um dos arquivos abaixo para remover:\n{arquivo_por_linha}")
                arquivo_p_remover = input("Digite (ou copie e cole) o nome do arquivo a ser removido:\n")
#DELETAR
                deletar_arquivo(arquivo_p_remover)
                historico_geral = lista_arquivos("treino-crossfit", ".txt", ".")
#SUAS METAS
        elif opcoes_usuario == 5:
            while True:
                add_remove = int(input("O que você deseja fazer? 1-Adicionar meta 2-Concluir meta 3-Visualizar progresso 4-SAIR: "))
                if add_remove == 1:
                    quantidade_metas=int(input("Digite a quantidade de metas que deseja adcionar: "))
                    for i in range(quantidade_metas):
                        meta_nova = metas.append(input(f"Digite sua meta {i+1}: "))                       
                elif add_remove == 2:
                    print("\nSUAS METAS:")
                    for i, meta in enumerate(metas,start=1):
                        print(f"{i}-{meta}")
                    
                    quantidade_metas_concluidas = int(input("Quantas metas foram concluidas? "))
                    indices_para_remover = []
                    for i in range(quantidade_metas_concluidas):
                        conclusao = int(input("Digite o número de uma meta concluida: "))
                        indices_para_remover.append(conclusao - 1)
                        
                    indices_para_remover.sort(reverse=True)

                    for indice in indices_para_remover:
                        metas_concluidas.append(metas[indice])
                        metas.pop(indice)
                        
                elif add_remove == 3:
                    print("\nMETAS:")
                    for meta in metas:
                        print(meta)
                    print("\nMETAS_CONCLUIDAS:")
                    for avanco in metas_concluidas:
                        print(f"{avanco}")
                    
                elif add_remove == 4:
                    break
                else:
                    print("Essa opção não existe.")

#SUA PLAYLIST   
        elif opcoes_usuario == 6:
            print("Playlist para o seu mood:\n1-Feliz\n2-Triste\n3-Dangerous Woman\n4-The G.O.A.T\n5- Charlie Brown Jr. (As melhores)\n6-Taylor Swift (A maior)")
            playlists = int(input("Qual o seu mood pro seu treino de hoje?"))
            print(escolha_playlists(playlists))

#SUGESTÃO
        elif opcoes_usuario == 7:
            sugerir_wod()

#ENCERRAR
    except Exception as e:
        print(f"Erro: {e}")
        break
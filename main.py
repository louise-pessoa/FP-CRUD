import os

os.system('cls')
historico_geral = []

def adicionar_no_arquivo(movimentos, data, tempo, tipo, data_conteudo):
        with open(f"treino-crossfit{data}.txt", "w", encoding='utf8') as arquivo:
            movimentos_lista = [movimentos.capitalize() for movimentos in movimentos.split(", ")]
            arquivo.write("Data: " + data_conteudo + "\nDuração: " + tempo + " minutos\nTipo de treino: " + tipo)
            arquivo.write("\nMovimentos:\n")

            for i in range(len(movimentos_lista)):
                arquivo.write(str(i+1) + ". " + movimentos_lista[i] + "\n")
            
def lista_arquivos(comeco, fim, caminho):
    try:
        historico_treinos = []
        for arquivo in os.listdir(caminho):
            if arquivo.startswith(comeco) and arquivo.endswith(fim):
                historico_treinos.append(arquivo)
        historico_treinos.reverse()
    except FileNotFoundError:
        print("Arquivo não encontrado.")

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
def filtragem():
    return

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
    historico_treinos2 = lista_arquivos("treino-crossfit", ".txt", ".")
    for arquivo in historico_treinos2:
        if arquivo == arquivo_escolhido:
            historico_treinos2.remove(arquivo)

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



while True:
    
    try:
#CRIAR
        print("/\\" * 15)
        opcoes_usuario = int(input("""\nEscolha uma ação:\n1- Adicionar\n2- Visualizar\n3- Editar\n4- Deletar\n5- Suas metas\n6- Sua playlist
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
                #sugestão: buscar por mes ou ano
            else:
                print("Opção inválida")


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
                #mudar data no CONTEÚDO do arquivo
                edicao_split = edicao.split()
                edicao_conteudo = "/".join(edicao_split)
                arquivo_p_editar = editar_arquivo(arquivo_p_editar, opcao_edicao, edicao_conteudo)

                #mudar data no NOME do arquivo
                edicao_nome = "".join(edicao_split)
                os.rename(arquivo_p_editar, f'treino-crossfit{edicao_nome}.txt')
                print(historico_geral)
                #historico_geral.sort()
                #print(historico_geral)

            elif opcao_edicao == 2 or opcao_edicao == 3:
                #mudar tempo de duração ou tipo de treino
                arquivo_p_editar = editar_arquivo(arquivo_p_editar, opcao_edicao, edicao)

            elif opcao_edicao == 4:
                #mudar movimentos do treino
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
        elif opcoes_usuario == 5:
            quantidade_metas=int(input("Digite a quantidade de metas que deseja adcionar: "))
            metas = []
            metas_concluidas = []
            for i in range(quantidade_metas):
                metas.append(input("Digite sua meta: "))
            for arquivo in historico_geral:
                with open(arquivo, "r" , encoding="utf-8") as treino:
                    conteudo = treino.read()
                    if conteudo in metas:
                        metas_concluidas.append(conteudo)
                        metas.remove(conteudo)
            print(f"METAS:  {metas}")
            print(f"METAS CONCLUIDAS:  {metas_concluidas}")
        
        elif opcoes_usuario == 6:
            print("Playlist para o seu mood:\n1-Feliz\n2-Triste\n3-Dangerous Woman\n4-The G.O.A.T\n5- Charlie Brown Jr. (As melhores)\n6-Taylor Swift (A maior)")
            playlists = int(input("Qual o seu mood pro seu treino de hoje?"))
            print(escolha_playlists(playlists))
           

                


#ENCERRAR
    except Exception as e:
        print(f"Erro: {e}")
        break
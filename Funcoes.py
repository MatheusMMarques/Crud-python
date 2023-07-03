def cadastrar_cliente():
    try:
        with open('Dados.txt', 'a') as arquivo:
            codigo = input("Digite seu código de cadastro: ")
            nome = input("Digite seu nome: ")
            endereco = input("Digite seu endereço: ")
            bairro = input("Digite seu bairro: ")
            cidade = input("Digite sua cidade: ")

            cliente = f"{codigo},{nome},{endereco},{bairro},{cidade}\n" #definindo uma variavel para armazenar os dados como dicionário
            arquivo.write(cliente)
            print("Dados do cliente cadastrados com sucesso!\n")
    except Exception as e:
        print("Ocorreu um erro ao cadastrar os dados:", str(e))

def listar_dados():
    try:
        with open('Dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()


            if not linhas:
                print("Nenhum dado de cliente cadastrado.")
            else:
                print("Dados dos clientes cadastrados:")
                for linha in linhas:
                    dados = linha.strip().split(',')
                    print("Código:", dados[0]) #Listando cada dado de acordo com sua locação
                    print("Nome:", dados[1])
                    print("Endereço:", dados[2])
                    print("Bairro:", dados[3])
                    print("Cidade:", dados[4])
                    print("--------------------")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao listar os dados:", str(e))

def alterar_dados():
    try:
        with open('Dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        if not linhas:
            print("Nenhum dado de cliente cadastrado.")
            return
        
        codigo = input("Digite o código do cliente que deseja alterar: ")
        encontrado = False

        with open('Dados.txt', 'w') as arquivo:
            for linha in linhas: #lendo linha por linha para fazer a alteração
                dados = linha.strip().split(',')
                if dados[0] == codigo:
                    novo_nome = input("Digite o novo nome do cliente: ")
                    novo_endereco = input("Digite o novo endereço: ")
                    novo_bairro = input("Digite o novo bairro: ")
                    nova_cidade = input("Digite a nova cidade: ")

                    nova_linha = f"{dados[0]},{novo_nome},{novo_endereco},{novo_bairro},{nova_cidade}\n"
                    arquivo.write(nova_linha) #implementando alterações
                    encontrado = True
                    print("Dados do cliente alterados com sucesso!\n")
                else:
                    arquivo.write(linha)
                
        if not encontrado:
            print("Nenhum cliente encontrado com o código fornecido.")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
    except Exception as e:
        print("Ocorreu um erro ao alterar os dados.", str(e))

def excluir_dados():
    try:
        with open('Dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        
        if not linhas:
            print("Nenhum dado de cliente encontrado.\n")
            return  
        
        codigo = input("Digite o código do cliente que deseja excluir: ")
        encontrado = False

        with open('Dados.txt', 'w') as arquivo:
            for linha in linhas:
                dados = linha.strip().split(',')
                if dados[0] == codigo:
                    encontrado = True
                    print("Dados do cliente excluidos com sucesso!\n")
                else:
                    arquivo.write(linha)

        if not encontrado:
            print("Nenhum cliente encontrado com o código fornecido.\n")
    except FileNotFoundError:
            print("Arquivo de dados não encontrado.\n")
    except Exception as e:
            print("Ocorreu um erro ao excluir os dados.", str(e))

def realizar_backup():
    try:
        with open('Dados.txt', 'r') as arquivo_origem:
            with open('backup_Dados.txt', 'w') as arquivo_backup:
                conteudo = arquivo_origem.read()
                arquivo_backup.write(conteudo) #inserindo conteudo do arquivo origem para arquivo backup
        print("Backup do arquivo realizado com sucesso!\n")
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.\n")
    except Exception as e:
        print("Ocorreu um erro ao realizar o backup.\n")
        
def exibir_menu():
    while True:

        print("1- Cadastrar Dados")
        print("2- Listar dados")
        print("3- Alterar dados")
        print("4- Excluir dados")
        print("5- Realizar Backup do arquivo")
        print("0- Sair\n")

        escolha = int(input("Digite a opção desejada: "))

        if (escolha == 1):
            cadastrar_cliente()

        elif (escolha == 2):
            listar_dados()

        elif (escolha == 3):
            alterar_dados()

        elif (escolha == 4):
            excluir_dados()

        elif (escolha == 5):
            realizar_backup()

        elif (escolha == 0):
            print ("Você saiu.")
            print ("Obrigado pelo contato.")
            break
        
        else:
            print("Opção invalida, Digite um dos números solicitados.")



                        

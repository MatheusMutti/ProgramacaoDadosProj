import csv

# Carregamento de dados

with open('steam_games.csv', newline='', encoding='UTF-8') as csvfile:
    leitor = csv.DictReader(csvfile)

    colunas = leitor.fieldnames
    
# Criar funções para procurar objetivos do trabalho

# Pergunta 1: Qual o percentual de jogos gratuitos e pagos na plataforma?
    # Criar contador

    countFreeGames = 0
    countPaidGames = 0

    # Iterar sobre todos os produtos

    for linha in leitor:
        price = linha.get('Price')
        if price == '0.0': countFreeGames+=1
        else : countPaidGames+=1 
        
    # Fazer percentual

    total = countPaidGames + countFreeGames
    percentualFreeGames = (countFreeGames / total) * 100
    print(f"O número total de jogos na plataforma é de {total}, os jogos que gratuitos contabilizam {countFreeGames}, enquanto os pagos {countPaidGames}. Desta forma, o percentual de jogos grátis é de {percentualFreeGames:.2f}%.")
    
# Pergunta 2: Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados.

    # Criação de variáveis

    csvfile.seek(0)
    next(leitor)
    
    datas = {}
    
    # Iterar sobre linhas

    for linha in leitor:

    # Tratar string para somente acessar o ano

        dataString = linha.get('Release date')
        dataInt = int(dataString[-4:])

    # Lógica para manipular o dicionário e maior valor de lançamento

        if dataInt not in datas:
            datas[dataInt] = 1
        else : datas[dataInt] += 1

        anoMaisLancamentos = max(datas, key=datas.get)
        maiorValor = datas[anoMaisLancamentos]


    # Print resultado

    print(f"O ano com maior número de lançamentos foi {anoMaisLancamentos}, com o valor de {maiorValor} jogos.")    

    # Pergunta 3:  Jogos com maior Concurrent Users, dentre os jogos pagos e os jogos gratuitos.

    # Criação variáveis

    csvfile.seek(0)
    next(leitor)
    maiorNumUsersFree = 0
    maiorNumUsersPaid = 0
    nomeMaiorJogoFree = None
    nomeMaiorJogoPaid = None


    # Iterando sobre o arquivo

    for linha in leitor:
        ccu = int(linha.get('Peak CCU'))
        nome = linha.get('Name')
        price = linha.get('Price')

    # Lógica para diferenciação dos jogos

        if price == '0.0':
            if ccu > maiorNumUsersFree:
                maiorNumUsersFree = ccu
                nomeMaiorJogoFree = nome 
        else : 
            if ccu > maiorNumUsersPaid:
                maiorNumUsersPaid = ccu
                nomeMaiorJogoPaid = nome 


    print(f"O jogo gratuito com o maior número de jogadores foi {nomeMaiorJogoFree}, com o total de {maiorNumUsersFree}\nEnquanto o jogo pago com o maior número de jogadores foi {nomeMaiorJogoPaid}, com um total de {maiorNumUsersPaid}")


# Funções adicionais

    # Selecionar 20 jogos aleatórios

# Elaborar testes

# Retorno das informações deve fazer sentido (número de campos)
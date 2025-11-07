import csv

# Carregamento de dados

with open('steam_games.csv', newline='', encoding='UTF-8') as csvfile:
    leitor = csv.DictReader(csvfile)

    colunas = leitor.fieldnames
    
    '''for linha in leitor:
        nome = linha.get('Name')
        price = linha.get('Price')
        print(price)
        if price == '19.99': print('got it')
        print(price)
        break'''

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
    print(f"O número total de jogos na plataforma é de {total}, os jogos que gratuitos contabilizam {countFreeGames}, enquanto os pagos {countPaidGames}. Desta forma, o percentual de jogos grátis é de {percentualFreeGames}.")
    #TODO 
    #Arrumar percentual para duas casas decimais.


    # Pergunta 2: Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados. 
        #Iterar sobre linhas usando um contador
        #Caso seja o maior, guardar informação do ano.
        #Caso empate, armazenar ano em uma lista

    #Pergunta 3:  Para demonstrar a facilidade de revisão e modificação de uso do módulo desenvolvido, uma pergunta adicional deve ser proposta e respondida por você. 
        #Jogos com maior "Avarage playtime forever"

# Funções adicionais

    # Iterar sobre os jogos (args -> dicionário e condição a ser procurada)

    # Selecionar 20 jogos aleatórios

    # Procurar jogo pelo nome

    # Retornar todos os dados de determinado jogo

# Elaborar testes

    # Retorno das informações deve fazer sentido (número de campos)

    #


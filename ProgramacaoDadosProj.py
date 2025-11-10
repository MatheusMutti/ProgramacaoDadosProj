import csv

# Pergunta 1: Qual o percentual de jogos gratuitos e pagos na plataforma?

def calcular_percentual_jogos_gratuitos(arquivo):
    with open(arquivo, newline='', encoding='UTF-8') as csvfile:
        leitor = csv.DictReader(csvfile)
    
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

        return {
                'total': total,
                'free': countFreeGames,
                'paid': countPaidGames,
                'percentual_free': percentualFreeGames
            }
        
# Pergunta 2: Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados.

def encontrar_ano_mais_lancamentos(arquivo):
    with open(arquivo, newline='', encoding='UTF-8') as csvfile:
        leitor = csv.DictReader(csvfile)
    
    # Criação de variáveis
         
        datas = {}
    
    # Iterar sobre linhas

        for linha in leitor:
            
    # Tratar string para somente acessar o ano

            dataString = linha.get('Release date')
            if dataString and len(dataString) >= 4:
                dataInt = int(dataString[-4:])

    # Lógica para manipular o dicionário e maior valor de lançamento
            
                try:
                    if dataInt not in datas:
                        datas[dataInt] = 1
                    else : datas[dataInt] += 1
                except ValueError:
                    continue

        anoMaisLancamentos = max(datas, key=datas.get)
        maiorValor = datas[anoMaisLancamentos]
        anos_empatados = [ano for ano, qtd in datas.items() if qtd == maiorValor]
            
    # Print resultado

        return {
            'ano': anoMaisLancamentos,
            'quantidade': maiorValor,
            'empates': anos_empatados if len(anos_empatados) > 1 else []
        }

# Pergunta 3:  Jogos com maior Concurrent Users, dentre os jogos pagos e os jogos gratuitos.

def encontrar_jogos_maior_ccu(arquivo):
    with open(arquivo, newline='', encoding='UTF-8') as csvfile:
        leitor = csv.DictReader(csvfile)

    # Criação variáveis

        maiorNumUsersFree = 0
        maiorNumUsersPaid = 0
        nomeMaiorJogoFree = None
        nomeMaiorJogoPaid = None

    # Iterando sobre o arquivo

        for linha in leitor:
            try:    
                ccu = int(linha.get('Peak CCU'))
                nome = linha.get('Name')
                price = linha.get('Price')

    # Lógica para diferenciação dos jogos

                if price == '0.0':
                    if ccu > maiorNumUsersFree:
                        maiorNumUsersFree = ccu
                        nomeMaiorJogoFree = nome 
                else: 
                    if ccu > maiorNumUsersPaid:
                        maiorNumUsersPaid = ccu
                        nomeMaiorJogoPaid = nome 
            except (ValueError, TypeError): 
                continue

        return {
            'free_game': nomeMaiorJogoFree,
            'free_ccu': maiorNumUsersFree,
            'paid_game': nomeMaiorJogoPaid,
            'paid_ccu': maiorNumUsersPaid
        }

# Execução do programa

if __name__ == "__main__":
    arquivo = 'steam_games.csv'
    
    # Pergunta 1
    resultado1 = calcular_percentual_jogos_gratuitos(arquivo)
    print(f"Total: {resultado1['total']}, Gratuitos: {resultado1['free']}, Pagos: {resultado1['paid']}, Percentual Free: {resultado1['percentual_free']:.2f}%.")
    
    # Pergunta 2
    resultado2 = encontrar_ano_mais_lancamentos(arquivo)
    if resultado2['empates']:
        print(f"Anos empatados: {resultado2['empates']} com {resultado2['quantidade']} jogos.")
    else:
        print(f"Ano com mais lançamentos: {resultado2['ano']} com {resultado2['quantidade']} jogos.")
    
    # Pergunta 3
    resultado3 = encontrar_jogos_maior_ccu(arquivo)
    print(f"Jogo free com maior CCU: {resultado3['free_game']} com o total de {resultado3['free_ccu']}.")
    print(f"Jogo pago com maior CCU: {resultado3['paid_game']} com o total de {resultado3['paid_ccu']}.")
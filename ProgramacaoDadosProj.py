import csv

#Fase 1

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

# Fase 2

# Pergunta 1: No caso de notas repetidas, ordenar o jogo de acordo com sua data de lançamento. (Mais velho para o mais recente)
# falta ordenar por data se for a mesma nota
def encontrar_jogos_mais_bem_avaliados(arquivo):
    with open(arquivo, newline='', encoding='UTF-8') as csvfile:
        leitor = csv.DictReader(csvfile)
    
    # Criação de classe e funções
         
        class DicionarioLimitado:

            def __init__(self, limite=10):
                self._dictDados = {}
                self.limite = limite

            def setItem(self, chave, valor):
                if chave in self._dictDados:
                    self._dictDados[chave] = valor
                    return
                
                if len(self._dictDados) < self.limite:
                    self._dictDados[chave] = valor
                    return
                
                menor_nota = min(self._dictDados.values())
                
                # Só adiciona se a nova nota for maior que a menor nota atual
                if valor > menor_nota:
                    for key, val in self._dictDados.items():
                        if val == menor_nota:
                            del self._dictDados[key]
                            break
                    self._dictDados[chave] = valor

            def tamanhoDict(self):
                return len(self._dictDados)
            
            def getDict(self):
                return self._dictDados
            
            def getMinValue(self):
                if self._dictDados:
                    return min(self._dictDados.values())
                return None
            
        meu_dict = DicionarioLimitado(10)
    
    # Iterar sobre linhas

        for linha in leitor:
            
    # Lógica para comparar jogos e adicionar no dictionario

            try:
                notaJogo = int(linha.get('Metacritic score', 0))
                nomeJogo = linha.get('Name', '')

                if nomeJogo:
                    meu_dict.setItem(nomeJogo, notaJogo)
            
            except (ValueError, TypeError):
                continue

        dict_ordenado = dict(sorted(meu_dict.getDict().items(), 
                                  key=lambda item: item[1], 
                                  reverse=True))
        return dict_ordenado


# Pergunta 2: Para jogos de role-playing, qual o número médio e máximo de: DLCs, avaliações positivas, avaliações negativas e materiais de demonstração (número de capturas de tela e filmes, somados)?  

def encontrar_jogos_de_rpg(arquivo):
    with open(arquivo, newline='', encoding='UTF-8') as csvfile:
        leitor = csv.DictReader(csvfile)

        jogosRPG = 0
        valorTotalMidia = 0
        valorTotalMediaDLC = 0
        valorTotalAvalPositivas = 0
        valorTotalAvalNegativas = 0

        # Declaração dos valores máximos

        numMaximoDeMidiasRpg = 0        
        numMaximoDLC = 0
        numMaximoAvalPositivas = 0
        numMaximoAvalNegativas = 0

    #Iterar sobre os jogos, procurando dados nas colunas

        for linha in leitor:
            
            try:

                colunaDLC = int(linha.get('DLC count', 0))
                avaiacoesPositivas = int(linha.get('Positive', 0))
                avaiacoeNegativas = int(linha.get('Negative', 0))
                
                # Manipulação de strings

                ColunaTags = linha.get('Tags')
                printsMateriaisDemo = linha.get('Screenshots')
                moviesMateriaisDemo = linha.get('Movies')
                
                resultadoTags = ColunaTags.split(',')                
                resultadoImagens = printsMateriaisDemo.split(',')
                resultadoMovies = moviesMateriaisDemo.split(',')
                
                quantidadeImagens = len(resultadoImagens)
                quantidadeMovies = len(resultadoMovies)
                quantidadeDeMidia = int(quantidadeImagens) + int(quantidadeMovies)

                # Armazenando resultados numéricos máximos
            
                if 'RPG' in resultadoTags:
                    jogosRPG=+1
                    if quantidadeDeMidia > numMaximoDeMidiasRpg: numMaximoDeMidiasRpg = quantidadeDeMidia
                    if colunaDLC > numMaximoDLC : numMaximoDLC = colunaDLC
                    if avaiacoesPositivas > numMaximoAvalPositivas: numMaximoAvalPositivas = avaiacoesPositivas
                    if avaiacoeNegativas > numMaximoAvalNegativas: numMaximoAvalNegativas = avaiacoeNegativas

                # Armazenamento valores totais para cálculo

                    valorTotalMidia+= quantidadeDeMidia
                    valorTotalMediaDLC+= colunaDLC
                    valorTotalAvalPositivas+= avaiacoesPositivas
                    valorTotalAvalNegativas+= avaiacoeNegativas
                    
                # Calculo Medias

                    MediaMidiasRpg = jogosRPG / valorTotalMidia
                    try:
                        MediaDLC = jogosRPG / valorTotalMediaDLC
                    except (ValueError, TypeError, ZeroDivisionError):
                        continue
                    MediaAvalPositivas = jogosRPG / valorTotalAvalPositivas
                    MediaAvalNegativas = jogosRPG / valorTotalAvalNegativas

            except (ValueError, TypeError):
                continue

        return {
            'total_midia': valorTotalMidia,
            'total_DLC': valorTotalMediaDLC,
            'total_positivas': valorTotalAvalPositivas,            
            'total_negativas': valorTotalAvalNegativas,
            'media_midia': MediaMidiasRpg,
            'media_DLC': MediaDLC,
            'medial_positivas': MediaAvalPositivas,
            'media_negativas': MediaAvalNegativas
        }

# Pergunta 3: Quais são as cinco empresas que mais publicam jogos pagos na plataforma? Para as empresas, qual o número médio e mediano de avaliações positivas nos seus jogos pagos?

def encontrar_empresas(arquivo):
    with open(arquivo, newline='', encoding='UTF-8') as csvfile:
        leitor = csv.DictReader(csvfile)

        #coluna = 'Developers'


# Pergunta 4: O numero de jogos que suportam o sistema Linux cresceu entre 2018 e 2022?

def encontrar_jogos_linux(arquivo):
    with open(arquivo, newline='', encoding='UTF-8') as csvfile:
        leitor = csv.DictReader(csvfile)

        #coluna = 'Linux' - booleano


# Pergunta 5: A definir


# Gráficos

# Gráfico 1: Percentual de jogos que possuem suporte pra cada sistema operacional. Caso jogo aceite multiplos, contar um voto para cada sistema suportado.


# Gráfico 2: Número total de jogos single-player do genero indie e estratégia lançados por ano entre 2010 e 2020


# Gráfico 3: A definir


# Execução do programa

if __name__ == "__main__":
    arquivo = 'steam_games.csv'
    
    # Fase 1
    
    # Pergunta 1
    #resultado1 = calcular_percentual_jogos_gratuitos(arquivo)
    #print(f"Total: {resultado1['total']}, Gratuitos: {resultado1['free']}, Pagos: {resultado1['paid']}, Percentual Free: {resultado1['percentual_free']:.2f}%.")
    
    # Pergunta 2
    #resultado2 = encontrar_ano_mais_lancamentos(arquivo)
    #if resultado2['empates']:
    #    print(f"Anos empatados: {resultado2['empates']} com {resultado2['quantidade']} jogos.")
    #else:
    #    print(f"Ano com mais lançamentos: {resultado2['ano']} com {resultado2['quantidade']} jogos.")
    
    # Pergunta 3
    #resultado3 = encontrar_jogos_maior_ccu(arquivo)
    #print(f"Jogo free com maior CCU: {resultado3['free_game']} com o total de {resultado3['free_ccu']}.")
    #print(f"Jogo pago com maior CCU: {resultado3['paid_game']} com o total de {resultado3['paid_ccu']}.")

    # Fase 2

    # Pergunta 1
    #resultado21 = encontrar_jogos_mais_bem_avaliados(arquivo)
    #print("Top 10 jogos mais bem avaliados:")
    #for jogo, nota in resultado.items():
    #    print(f"{jogo}: {nota}")

    # Pergunta 2
    #resultado22 = encontrar_jogos_de_rpg(arquivo)
    #print(f"Número máximo de DLCs: {resultado22['total_DLC']:,} com a média de {resultado22['media_DLC']:.8f}.")
    #print(f"Número máximo de mídias : {resultado22['total_midia']:,} com a média de {resultado22['media_midia']:.8f}.")
    #print(f"Número máximo de avaliações positivas: {resultado22['total_positivas']:,} com a média de {resultado22['medial_positivas']:.8f}.")
    #print(f"Número máximo de avaliações negativas: {resultado22['total_negativas']:,} com a média de {resultado22['media_negativas']:.8f}.")

    # Pergunta 3
    

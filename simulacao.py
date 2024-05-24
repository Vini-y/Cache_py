from cache import LRU, LFU, FIFO, Users
from lib import puro, poisson, porcentagem
import time


def simulacao(algoritmoObj):
  # Inicializa uma lista de usuários para armazenar métricas de desempenho
  usuarios = [Users(), Users(), Users()]

  # Loop sobre cada usuário
  for usuario in usuarios:
    # Gera valores aleatórios usando diferentes métodos de geração
    gerador_de_aleatorio = [[puro() for i in range(0, 200)],
                            [poisson() for i in range(0, 200)],
                            [porcentagem() for i in range(0, 200)]]

    value = ""
    j = 0
    # Loop sobre cada conjunto de valores aleatórios gerados
    for j, aleatorios in enumerate(gerador_de_aleatorio):
        for i in aleatorios:
            start_time = time.time()  # Marca o tempo de início da operação
            value = algoritmoObj.get(i)  # Obtém o valor usando o algoritmo de cache especificado 
            print(value[0])# Marca o tempo de término da operação
            end_time = time.time()
            elapsed_time = end_time - start_time  # Calcula o tempo decorrido
            # Atualiza as métricas do usuário com base no resultado da operação
            if value[1] == 0:  # Se for um miss
                #usuario.addTimeMisses(elapsed_time)  # Adiciona o tempo de miss
                usuario.sumTimeMisses[j] += elapsed_time
                usuario.cacheMisses[j] += 1  # Incrementa o contador de misses
            else:  # Se for um hit
                usuario.sumTimeHits[j] += elapsed_time  # Adiciona o tempo de hit
                usuario.cacheHits[j] += 1  # Incrementa o contador de hits

      
    usuario.generateAverages()  # Calcula as médias de tempo de acesso

  return usuarios  # Retorna a lista de usuários com métricas de desempenho


def chamarSimulacao():

  a = LRU(10)
  users1 = simulacao(a)

  b = LFU(10)
  users2 = simulacao(b)

  c = FIFO(10)
  users3 = simulacao(c)

  with open('relatorio.txt', 'w') as arquivo:
    arquivo.write("Relatório de desempenho dos algoritmos de cache: \n\n")

    # Escrevendo para o algoritmo LRU
    arquivo.write("------------ LRU ------------ \n")
    for i, user in enumerate(users1, 1):
      arquivo.write(f"\nUsuario {i}: \n\n")
      
      arquivo.write("  Aleatório Puro: \n")
      arquivo.write(f"    Numero de cache misses: {user.cacheMisses[0]}\n")
      user.mediaTempoGeral[0] = (user.sumTimeHits[0] + user.sumTimeMisses[0]) / (
        user.cacheHits[0] + user.cacheMisses[0])
      arquivo.write(f"    Tempo médio gasto: {user.mediaTempoGeral[0]} segundos\n")

      arquivo.write("  Aleatório Poisson: \n")
      arquivo.write(f"    Numero de cache misses: {user.cacheMisses[1]}\n")
      user.mediaTempoGeral[1] = (user.sumTimeHits[1] + user.sumTimeMisses[1]) / (
        user.cacheHits[1] + user.cacheMisses[1])
      arquivo.write(f"    Tempo médio gasto: {user.mediaTempoGeral[1]} segundos\n")
      
      arquivo.write("  Aleatório com Porcentagem: \n")
      arquivo.write(f"    Numero de cache misses: {user.cacheMisses[2]}\n")
      user.mediaTempoGeral[2] = (user.sumTimeHits[2] + user.sumTimeMisses[2]) / (
        user.cacheHits[1] + user.cacheMisses[2])
      arquivo.write(f"    Tempo médio gasto: {user.mediaTempoGeral[1]} segundos\n\n")
      
      user.generateAverages()
      arquivo.write(f"  Tempo médio gasto hits: {user.mediTimeHits} segundos\n")
      arquivo.write(f"  Tempo médio gasto misses: {user.mediTimeMisses} segundos\n")
      arquivo.write(f"  Numero de cache hits: {sum(user.cacheHits)}\n")
      arquivo.write(f"  Numero de cache misses: {sum(user.cacheMisses)}\n")

      arquivo.write(f"  Tempo medio Usuario {i}: {sum(user.mediaTempoGeral)/3} segundos \n")
    arquivo.write(
        f"\nTempo medio geral do LRU: {(sum(users1[0].mediaTempoGeral)/3 + sum(users1[1].mediaTempoGeral)/3+     sum(users1[2].mediaTempoGeral)/3)/3} segundos \n"
    )

    # Escrevendo para o algoritmo LFU
    arquivo.write("\n------------ LFU ------------ \n")
    for i, user in enumerate(users2, 1):
      arquivo.write(f"\nUsuario {i}: \n\n")

      arquivo.write("  Aleatório Puro: \n")
      arquivo.write(f"    Numero de cache misses: {user.cacheMisses[0]}\n")
      user.mediaTempoGeral[0] = (user.sumTimeHits[0] + user.sumTimeMisses[0]) / (
        user.cacheHits[0] + user.cacheMisses[0])
      arquivo.write(f"    Tempo médio gasto: {user.mediaTempoGeral[0]} segundos\n")

      arquivo.write("  Aleatório Poisson: \n")
      arquivo.write(f"    Numero de cache misses: {user.cacheMisses[1]}\n")
      user.mediaTempoGeral[1] = (user.sumTimeHits[1] + user.sumTimeMisses[1]) / (
        user.cacheHits[1] + user.cacheMisses[1])
      arquivo.write(f"    Tempo médio gasto: {user.mediaTempoGeral[1]} segundos\n")

      arquivo.write("  Aleatório com Porcentagem: \n")
      arquivo.write(f"    Numero de cache misses: {user.cacheMisses[2]}\n")
      user.mediaTempoGeral[2] = (user.sumTimeHits[2] + user.sumTimeMisses[2]) / (
        user.cacheHits[1] + user.cacheMisses[2])
      arquivo.write(f"    Tempo médio gasto: {user.mediaTempoGeral[1]} segundos\n\n")

      user.generateAverages()
      arquivo.write(f"  Tempo médio gasto hits: {user.mediTimeHits} segundos\n")
      arquivo.write(f"  Tempo médio gasto misses: {user.mediTimeMisses} segundos\n")
      arquivo.write(f"  Numero de cache hits: {sum(user.cacheHits)}\n")
      arquivo.write(f"  Numero de cache misses: {sum(user.cacheMisses)}\n")

      arquivo.write(f"  Tempo medio Usuario {i}: {sum(user.mediaTempoGeral)/3} segundos \n")
    arquivo.write(
        f"\nTempo medio geral do LFU: {(sum(users2[0].mediaTempoGeral)/3 + sum(users2[1].mediaTempoGeral)/3+     sum(users2[2].mediaTempoGeral)/3)/3} segundos \n"
    )
    # Escrevendo para o algoritmo FIFO
    arquivo.write("\n------------ FIFO ------------ \n")
    for i, user in enumerate(users3, 1):
      
      arquivo.write(f"\nUsuario {i}: \n\n")

      arquivo.write("  Aleatório Puro: \n")
      arquivo.write(f"    Numero de cache misses: {user.cacheMisses[0]}\n")
      user.mediaTempoGeral[0] = (user.sumTimeHits[0] + user.sumTimeMisses[0]) / (
        user.cacheHits[0] + user.cacheMisses[0])
      arquivo.write(f"    Tempo médio gasto: {user.mediaTempoGeral[0]} segundos\n")

      arquivo.write("  Aleatório Poisson: \n")
      arquivo.write(f"    Numero de cache misses: {user.cacheMisses[1]}\n")
      user.mediaTempoGeral[1] = (user.sumTimeHits[1] + user.sumTimeMisses[1]) / (
        user.cacheHits[1] + user.cacheMisses[1])
      arquivo.write(f"    Tempo médio gasto: {user.mediaTempoGeral[1]} segundos\n")

      arquivo.write("  Aleatório com Porcentagem: \n")
      arquivo.write(f"    Numero de cache misses: {user.cacheMisses[2]}\n")
      user.mediaTempoGeral[2] = (user.sumTimeHits[2] + user.sumTimeMisses[2]) / (
        user.cacheHits[1] + user.cacheMisses[2])
      arquivo.write(f"    Tempo médio gasto: {user.mediaTempoGeral[1]} segundos\n\n")

      user.generateAverages()
      arquivo.write(f"  Tempo médio gasto hits: {user.mediTimeHits} segundos\n")
      arquivo.write(f"  Tempo médio gasto misses: {user.mediTimeMisses} segundos\n")
      arquivo.write(f"  Numero de cache hits: {sum(user.cacheHits)}\n")
      arquivo.write(f"  Numero de cache misses: {sum(user.cacheMisses)}\n")

      arquivo.write(f"  Tempo medio Usuario {i}: {sum(user.mediaTempoGeral)/3} segundos \n")
    arquivo.write(
        f"\nTempo medio geral do LRU: {(sum(users3[0].mediaTempoGeral)/3 + sum(users3[1].mediaTempoGeral)/3+     sum(users3[2].mediaTempoGeral)/3)/3} segundos \n"
    )

  # Calculando e escrevendo o tempo médio geral

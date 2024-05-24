import random
import numpy as np


def puro():
  numero = random.randint(1, 100)  #gerando um número aleatório entre 0 e 99
  return numero


def porcentagem():
  # Gerando uma quantidade aleatória entre 1 e 100
  quantidade = random.randint(1, 100)
  #33% do número gerado estar no intervalo de 30 a 40
  if quantidade <= 33:
    numero = random.randint(30, 40)
  else:
    # Se a quantidade for maior que 33%, o número gerado estará no intervalo de 1 a 99
    numero = random.randint(1, 100)
    #se estiver no intervalo de 30 a 40, um novo número é gerado até que esteja fora do intervalo
    while 30 <= numero <= 40:
      numero = random.randint(1, 100)

  return numero


def poisson():
  # Definindo o parâmetro lambda da distribuição de Poisson (taxa média de ocorrência)
  lambda_parameter = 50
  # Gerando 10 números aleatórios com distribuição de Poisson
  random_numbers = np.random.poisson(lambda_parameter)

  return random_numbers

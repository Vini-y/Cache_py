from collections import defaultdict


class Users:

  def __init__(self):
    # Inicializa as métricas de desempenho para hits
    self.cacheHits = [0, 0, 0]
    self.mediTimeHits = [0, 0, 0]
    self.sumTimeHits = [0.00, 0.00, 0.00]
    # Inicializa as métricas de desempenho para misses
    self.cacheMisses = [0, 0, 0]
    self.mediTimeMisses = [0.00]
    self.sumTimeMisses = [0.00,0.00,0.00]
    # [puro, poisson, porcentagem]

    self.mediaTempoGeral = [0.00, 0.00, 0.00]

  def addTimeHits(self, time):
    # Adiciona tempo de acesso ao cache para hits
    self.sumTimeHits += (time)

  def addTimeMisses(self, time):
    # Adiciona tempo de acesso ao cache para misses
    self.sumTimeMisses += (time)

  def generateAverages(self):
    # Calcula média de tempo de acesso para hits se houver hits registrados

    if sum(self.cacheHits) != 0:
      self.mediTimeHits = sum(self.sumTimeHits) / sum(self.cacheHits)
    else:
      print("no Hits")  # Mensagem se não houver hits registrados
      # Calcula média de tempo de acesso para misses se houver misses registrados
    if sum(self.cacheMisses) != 0:
      self.mediTimeMisses = sum(self.sumTimeMisses) / sum(self.cacheMisses)
    else:
      print("no Misses")  # Mensagem se não houver misses registrados


class LRU:

  def __init__(self, capacity):
    # Inicializa o cache com arquivos de texto e define sua capacidade
    self.cache = []
    for i in range(1, 11):
      self.cache.append((i, open(f"{i}.txt", "rt").read()))
    self.capacity = capacity

  def get(self, n_arquivo):

    i = 0
    hit = 0  # variável de controle para verificar hit ou miss, retornável na simulação
    conteudo = ""
    # Procura o arquivo no cache
    while hit == 0 and i < self.capacity:
      if self.cache[i][0] == n_arquivo:
        hit = 1
        conteudo = self.cache[i][1]
      i += 1
    # Se o arquivo não estiver no cache
    if not hit:
      conteudo = open(f"{n_arquivo}.txt",
                      "rt").read()  # Lê o arquivo do sistema de arquivos

    i -= 1
    self.cache.pop(i)  # Remove o arquivo mais antigo do cache
    self.cache.insert(
        0, (n_arquivo, conteudo))  # Adiciona o novo arquivo ao cache

    return conteudo, hit


class LFU:

  def __init__(self, capacity):
    # Inicializa o cache com arquivos de texto e define sua capacidade
    self.cache = {}
    for i in range(1, 11):
      self.cache[i] = [open(f"{i}.txt", "rt").read(), 0]
    self.capacity = capacity

  def get(self, n_arquivo):

    hit = 0  # variável de controle para verificar hit ou miss, retornável na simulação
    conteudo = ""

    if n_arquivo in self.cache:  # Se o arquivo estiver no cache
      self.cache[n_arquivo][1] += 1  # Incrementa o contador de acessos
      conteudo = self.cache[n_arquivo][0]
      hit = 1
    else:  # Se o arquivo não estiver no cache
      if len(self.cache) >= self.capacity:  # Se o cache estiver cheio
        menos_acessado = min(self.cache, key=lambda k: self.cache[k][1]
                             )  # Encontra o arquivo menos acessado
        del self.cache[
            menos_acessado]  # Remove o arquivo menos acessado do cache
      conteudo = open(
          f"{n_arquivo}.txt").read()  # Lê o arquivo do sistema de arquivos

      self.cache[n_arquivo] = [conteudo, 0]  # Adiciona o novo arquivo ao cache

    return conteudo, hit


class FIFO:

  def __init__(self, capacity):
    # Inicializa o cache com arquivos de texto e define sua capacidade
    self.capacity = capacity
    self.cache = {}
    for i in range(1, 11):
      self.cache[i] = [i, open(f"{i}.txt", "rt").read()]

  def get(self, n_arquivo):

    hit = 0  # variável de controle para verificar hit ou miss, retornável na simulação
    conteudo = ""

    if n_arquivo in self.cache:  # Se o arquivo estiver no cache
      conteudo = self.cache[n_arquivo][
          1]  # Obtém o conteúdo do arquivo do cache
      hit = 1
    else:  # Se o arquivo não estiver no cache
      if len(self.cache) >= self.capacity:  # Se o cache estiver cheio
        del self.cache[next(iter(
            self.cache))]  # Remove o arquivo mais antigo do cache
      conteudo = open(
          f"{n_arquivo}.txt").read()  # Lê o arquivo do sistema de arquivos

      self.cache[n_arquivo] = [n_arquivo,
                               conteudo]  # Adiciona o novo arquivo ao cache

    return conteudo, hit

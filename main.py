from simulacao import chamarSimulacao  # importando o arquivo simulação e a função chamarSimulação
from cache import LRU  # importando o arquivo cache e a classe LRU

control = True  #variável de controle para o while
while control:
  print(
      "\n\n (-1 ) Modo de simulação;\n ( 0 ) Encerrar;\n (1 a 100) Acessar arquivo.\n"
  )  #menu de opções
  option = int(input("Insira sua opção: "))  #input da opção

  if 1 <= option <= 100:  # se a opção estiver entre 1 e 100, acessará o arquivo e apresentará ao usuário
    value = LRU(10).get(option)  # carregando o algoitmo de LRU para uso do cache
    print(value[0])  # apresentando o conteúdo do arquivo ao usuário

  elif option == 0:  # se a opção for 0, encerrará o programa
    print("\nEncerrando o programa...")
    control = False  # variável de controle se torna falso
  elif option == -1:  # se a opção for -1, entrará em modo de simulação
    print("\nEntrando em modo de simulação...")
    chamarSimulacao()  # função para chamar a simulação
    print("\nRelatório gerado com sucesso!")
  else:  # se  a opção não atender nenhuma das condições anteriores
    print("\nNúmero de arquivo indisponível ou opção inválida! Tente novamente.")

# Grupo RA1 7
# Ana Flávia Martins dos Santos
# Isabella Vanderlinde Berkembrock
# Vinícius Yamamoto Borges
# Vitor Nicoletti

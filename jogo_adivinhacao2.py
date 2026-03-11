# Importa o módulo 'random', que fornece funções para gerar números aleatórios
import random

# Gera um número aleatório entre 1 e 10 usando a função randint
# randint(a, b) retorna um número inteiro entre 'a' e 'b' (inclusive)
numero_secreto = random.randint(1, 10)

# Inicializa o contador de tentativas do jogador
tentativas = 0

# Define o número máximo de tentativas permitidas
max_tentativas = 5

# Mensagens iniciais para o jogador
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando, entre 1 e 10.")

# Loop principal do jogo: continua enquanto o número de tentativas for menor que o máximo
while tentativas < max_tentativas:
    # Captura a entrada do usuário e converte para inteiro
    palpite = int(input("Digite seu palpite: "))

    # Incrementa o número de tentativas após cada palpite
    tentativas += 1

    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        # Caso o jogador acerte, exibe mensagem de vitória e encerra o loop
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break
    # Caso o palpite seja menor que o número secreto
    elif palpite < numero_secreto:
        print("Quase lá! Tente um número maior.")
    # Caso o palpite seja maior que o número secreto
    else:
        print("Quase lá! Tente um número menor.")

    # Informa ao jogador quantas tentativas restam, se ainda houver
    if tentativas < max_tentativas:
        print(f"Você tem {max_tentativas - tentativas} tentativas restantes.")

# Caso o jogador não acerte dentro do limite de tentativas
else:
    print("Infelizmente, você não acertou. O número era", numero_secreto)
    print("Fim do jogo!")

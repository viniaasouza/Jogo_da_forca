import random

def jogar():

    boas_vindas()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertada(palavra_secreta)

    enforcou = False
    acertou = False
    tentativas: int = 0


    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):# se a letra chutada está contida na palavra secreta, faça:
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)

        else:
            tentativas += 1
            desenha_forca(tentativas)

        enforcou = 7 == tentativas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)



def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0  # indice para andar na palavra secreta
    for i in palavra_secreta:  # laço verificando a posição da letra
        if (chute == i):  # se a letra digitada M/m for igual a da letra onde o i estiver na palavra secreta
            letras_acertadas[index] = i  # salve em um array na posição index de acordo com o que estiver em i.
        index = index + 1  # ande mais uma posição index

def pede_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()  # aqui ta apagando qualquer espaço que venha junto com a letra
    return chute

def boas_vindas():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo: #esse laço vai percorrer o txt
        linha = linha.strip() #aqui ele vai pegar as palavras dentro do txt e tirar toda a impureza, tipo o \n
        palavras.append(linha) #dentro da lista palavras, vai adicionar o conteudo txt linha a linha em strings

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertada(palavra):
    return ["_" for letra in palavra]

if(__name__ == "__main__"):
    jogar()


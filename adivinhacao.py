import  random

def jogar():

    print("**************************")
    print("Bem vindo ao jogo de adivinhacao")
    print("***************************")

    numero_secreto = random.randrange(1, 101) # a função randon gera numero entre 0.0 e 100
    total_de_tentativas = 0
    pontos = 1000


    print("Qual nivel de dificuldade?")
    print("(1) Fácil (2) Medio (3) Dificil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel ==2):
        total_de_tentativas = 20
    else:
        total_de_tentativas = 5

    print(numero_secreto)
    for rodada in range(1, total_de_tentativas +1 ):
        print("Tentativa {} de {}:" .format(rodada,  total_de_tentativas))
        chute_str = input("Digite o seu numero entre1 e 100: ")
        print("Você digitou ",chute_str)
        chute = int(chute_str)


        if(chute < 1 or chute > 100):
            print("Você deveria digitar um numero entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o numero secreto!")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o numero secreto!")
            pontos_perdidos = abs(numero_secreto - chute) #40-20 = 20 pontos perdidos
            pontos = pontos - pontos_perdidos

        rodada = rodada +1
if(__name__== "__main__"):
    jogar()
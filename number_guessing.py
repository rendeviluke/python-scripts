from logging import exception
import random
import string

def jogar():

    print("Bem-vindo ao joguinho em Python")

    numeroSecreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000
    

    print("Selecione um nivel:")
    print("1- Facil 2- Medio 3- Dificil")
    
    while True:
        try:
            nivel = int(input("Defina o nivel: "))
            while(nivel < 1 or nivel > 3):
                print("Erro: a dificuldade é de 1 a 3...")
                nivel = int(input("Defina o nivel: "))
            break
        except Exception as e:
                print("Apenas digite numeros inteiros...")

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    elif(nivel == 3):
        tentativas = 5

    
    for rodada in range (1, tentativas):
        print("Tentativa {} de {}".format(rodada, tentativas))
        
        while True:
            try:
                chute = int(input("Insira um numero: "))
                while chute < 1 or chute > 100:
                    print("Chute entre 1 e 100...")
                    chute = int(input("Insira um numero: "))
                    
                    print(f'Voce inseriu', chute)
                         
                break
            except Exception as e:
                print("Apenas digite numeros...")

        acertou = chute == numeroSecreto
        maior = chute > numeroSecreto
        menor = chute < numeroSecreto      
        

        if(acertou):
            print("Voce acertou e fez {} pontos!".format(pontos))
            print("Fim do jogo!")
            break
        else:
            print("Voce errou!")
                    
        if(maior):
            print("Seu chute foi maior que o numero secreto")
            
        elif(menor):
            print("Seu chute foi menor que o numero secreto")

        if(chute != True):
            chute = tentativas - 1


            pontosPerdidos = abs(numeroSecreto - chute)
            pontos = pontos - pontosPerdidos

if(__name__ == "__main__"):
    jogar()
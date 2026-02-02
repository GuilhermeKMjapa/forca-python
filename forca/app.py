#importando módulos
from palavras import palavras
import random

#seleção de palavras 
def seleciona_palavra():
    palavra = random.choice(palavras)
    return palavra.upper()

# iniciar o jogo
def jogar(palavra):
    #definir variaveis
    palavra_a_completar = "_" * len(palavra)
    adivinhou = False
    letras_uzadas = []
    palavra_uzada = []
    tentativas = 6

    # Boas vindas
    print("Vamos jogar!!!")
    print(exibir_tentativa(tentativas))
    print("Essa é a palavra %s" % palavra_a_completar)

    #Enquanto o usuario tiver vidas e ainda nao acertou
    while not adivinhou and tentativas > 0:

        tentativa = input("digite uma letra para continuar: ").upper()

        print(tentativa)

        #Tentativa de letra unica
        #Verificação de letras unicas
        if len(tentativa) == 1 and tentativa.isalpha():
            #Verificar se a letra ja foi utilizada
            if tentativa in letras_uzadas:
                print("Você já utilizou esta letra antes: %s" % tentativa)
            #Verificar se a tentativa é valida
            elif tentativa not in palavra:
                print("A letra %s não esta na palavra" % tentativa)
                tentativas -= 1
                letras_uzadas.append(tentativa)
                # Quando a letra não esta na palavra
            else:
                print("Você acertou! A letra %s está na palavra" % tentativa)    
                letras_uzadas.append(tentativa)
                # Transformar a palavra
                palavra_lista = list(palavra_a_completar)

                print(palavra_a_completar)

                # Verifica a posição dos _ e subistitui
                induces = [i for i, letra in enumerate(palavra) if letra == tentativa]
                for induce in induces:
                    palavra_lista[induce] = tentativa

                palavra_a_completar = "".join(palavra_lista)

                if "_" not in palavra_a_completar:
                    adivinhou = True
            # Tentativa de palavra completa
            # Quando o usuario tenta adivinhar a palavra
        elif len(tentativa) == len(palavra) and tentativa.isalpha():
        
            #Palavras utilizadas
            if tentativa in palavra_uzada:
                print("Você já utilizou está palavra %s" %tentativa)
            #palavra errada
            elif tentativa != palavra:
                print("A palavra %s está incorreta!" % tentativa)
                tentativas -= 1
                palavra_uzada.append(tentativa)
            #Acertou a palavra 
            else:
                adivinhou = True
                palavra_a_completar = palavra

        #Tentativa invalida 
        else:
            print("Tentativa invalida, tente novamente!")

        # Exibindo status do jogo
        print(exibir_tentativa(tentativas))
        print(palavra_a_completar)
    
    if adivinhou:
        print("Parabéns! Você ganhou o jogo")
    else:
        print("Não foi dessa vez, a palavra era: %s" % palavra)

# Status do jogo 
def exibir_tentativa(tentativas):
    estagios = [  # Fim de jogo
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
              # Falta 1 tentativa
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
              # Faltam 2 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
              # Faltam 3 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
              # Faltam 4 tentativas
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
              # Faltam 5 tentativas
              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
              # Estado inicial
              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
    ]
    
    return estagios[tentativas]

#inicio do jogo
def iniciar():
    palavra = seleciona_palavra()
    jogar(palavra)
    # Quando acaba o jogo, verifica se o usuário quer continuar jogando
    while input("Jogar novamente? (S/N)").upper() == "S":
        palavra = seleciona_palavra()
        jogar(palavra) 

iniciar()
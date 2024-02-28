print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#Definindo o número screto
numeroSecreto = 16


#Definindo o número de tentativas
numeroTentavivas = 3


while(numeroTentavivas >0):

#Recebendo o chute do jogador
    chuteString = input('Digite um número: ')
    print('Você digitou o número: ', chuteString)
    chute = int (chuteString)

#Declarando as condições
    if numeroSecreto == chute:
        print('Você acertou!')
    elif(chute>numeroSecreto):
        print('Voce errou!! O número secreto é numero menor')


    else:
        print('Você errou!! O numero secreto é um número maior')

    #Aula Elif 26.02.24

# Escreva um programa que pergunte a velocidade de um carro e a velocidade permitida e mostre:
# - A velocidade do carro
# - A porcentagem em que o carro ultrapassou a velocidade
# - Quantos pontos serão atribuídos na carteira
# - O tipo de infração (média, grave ou gravíssima)
# - O valor da multa.

# Considere os seguintes dados
# a) superior à máxima em até 20% : infração média (4 pontos) + multa no valor de R$ 130,16;
# b) superior à máxima permitida em mais de 20% até 50% : infração grave (5 pontos) + multa no valor de R$ 195,23;
# c) superior à máxima permitida em mais de 50% : infração gravíssima (7 pontos) + multa no valor de R$ 880,41+ suspensão da CNH e curso de reciclagem.

velocidadeVeiculo = int(input(' Digite a velocidade do veiculo: '))

velocidadeMax = 100

velocidadeUltrapassada = float((velocidadeVeiculo - velocidadeMax) / 100)

velocidadePorcentagem = int(f'{velocidadeUltrapassada * 100:.0f}') #andando a virgula, assim fica como no exemplo: 10



if (velocidadePorcentagem < 20):
    print(f' ====================================== \n Infração Média \n ====================================== \n A velocidade do veículo é de {velocidadeVeiculo}KM/H \n ====================================== \n Ultrapassou {velocidadePorcentagem}% a mais que o permitido \n ====================================== \n Serão adicionados 4 pontos \n ====================================== \n Multa no valor de R$130,16 \n ====================================== \n')

else: 
    if ((velocidadePorcentagem >= 20) and (velocidadePorcentagem < 50) ):
        print(f' ====================================== \n Infração Grave \n ====================================== \n A velocidade do veículo é de {velocidadeVeiculo}KM/H \n ====================================== \n Ultrapassou {velocidadePorcentagem}% a mais que o permitido \n ====================================== \n Serão adicionados 5 pontos \n ====================================== \n Multa no valor de R$195,23 \n ====================================== \n')

    else:
        if (velocidadePorcentagem >= 50):
            print(f' ====================================== \n Infração Gravíssima \n ====================================== \n A velocidade do veículo é de {velocidadeVeiculo}KM/H \n ====================================== \n Ultrapassou {velocidadePorcentagem}% a mais que o permitido \n ====================================== \n Serão adicionados 7 pontos \n ====================================== \n Multa no valor de R$880,41 \n ====================================== \n')


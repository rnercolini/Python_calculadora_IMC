# Calcula o Índice de Massa Corporal e classifica conforme faixa de IMC.
print('\033[4;31mCALCULADORA DO IMC\033[m')
print(' ')
peso = float(input('Digite o seu peso em quilos: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura ** 2)
print('\033[31m-+\033[m' * 30)
print('O seu IMC é de {:.1f}.'.format(imc))
print('\033[31m-+\033[m' * 30)
if imc < 18.5:
    print('Você está abaixo do peso, precisa se alimentar melhor.')
elif 18.5 <= imc < 25:
    print('Parabéns, você está com o peso ideal!')
elif 25 <= imc < 30:
    print('Atenção, você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Cuidado, você está com obesidade.')
else:
    print('Perigo, você está com obesidade mórbida.')


nome = input('Digite seu nome: ')
idade = int(input('Qual sua idade?: '))
altura = int(input('Qual sua altura?: '))
peso = float(input('Quanto você pesa?: '))

calc1 = altura * altura / 10000
calc2 = peso / calc1 

imc1 = 'menor que 18,5!' 
imc2 = 'entre 18,5 e 24,9!'
imc3 = 'entre 25 e 29,9!'
imc4 = 'entre 30 e 39,9!'
imc5 = 'maior que 40!'

if calc2 < 18.50: {
    print('Olá '+nome+', seu IMC está '+imc1+'\nClassificação: MAGREZA | OBESIDADE GRAU 0')
}
elif calc2 > 18.50 and calc2 < 24.90: {
    print('Olá '+nome+', seu IMC está '+imc2+'\nClassificação: NORMAL | OBESIDADE GRAU 0')
}
elif calc2 > 25 and calc2 < 29.90: {
    print('Olá '+nome+', seu IMC está '+imc3+'\nClassificação: SOBREPESO | OBESIDADE GRAU 1')
}
elif calc2 > 30 and calc2 < 39.90: {
    print('Olá '+nome+', seu IMC está '+imc4+'\nClassificação: OBESIDADE | OBESIDADE GRAU 2')
}
elif calc2 > 40: {
    print('Olá '+nome+', seu IMC está '+imc5+'\nClassificação: OBESIDADE GRAVE | OBESIDADE GRAU 3')
}
else: {
    print("Algo saiu errado..")
}
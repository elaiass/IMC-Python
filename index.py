peso = float(input('qual é o seu peso? (kg) '))
altura = float(input('qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('o IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do PESO normal')
elif 18.5 <= imc < 25:
    print('você está na faixa PESO ideal')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')

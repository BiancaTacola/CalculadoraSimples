"""algoritmo "Soma"
variáveis
    valor1, valor2, soma, divisao, subtracao, multiplicacao: real
início
    Escreva "Digite o primeiro valor"
    Leia valor1
    Escreva "Digite o segundo valor"
    Leia valor2
    soma = valor1 + valor2
    Escreva "A soma é ", soma
    subtracao = valor1 - valor2
    Escreva "A soma é ", subtracao
    divisao = valor1 / valor2
    Escreva "A soma é ", divisao
    multiplicacao = valor1 * valor2
    Escreva "A soma é ", multiplicacao
Fim"""

#Atribuindo valores as variaveis
valor1 = input("Por favor, digite o primeiro valor: ")
valor2 = input("Por favor, digite o segundo valor: ")

#Codigo para soma
soma = float(valor1) + float(valor2)
#Na soma devemos transformar o tipo de variavel de texto para numerico, para possibilitar uma soma
#para limitar o numero de casas decimais usamos o{:.numero de casas que queremosF}
print("A soma entre os valores é {:.0f}" .format(soma))

#Codigo para subtração
subtracao = float(valor1) - float(valor2)
print("A subtração entre os valores é {:.0f}".format(subtracao))

#Codigo para divisão
divisao = float(valor1) / float(valor2)
print("A divisão entre os valores é {:.2f}".format(divisao))

#Codigo para divisão inteira
divisao_inteira= float(valor1) // float(valor2)
print("A divisão inteira entre os valores é {:.2f}".format(divisao_inteira))

#Codigo para resto da divisão ou modulo
resto_divisao = float(valor1) % float(valor2)
print("Resto da divisão entre os valores é {:.2f}".format(resto_divisao))

#Codigo para mutiplicação
multiplicacao = float(valor1) * float(valor2)
print("A multiplicação entre os valores é {:.0f}".format(multiplicacao))


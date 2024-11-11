# Lista 02 Prática
# Questão 01 
numero = float(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou zero
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")


# Questão 02

idade = int(input("Digite a sua idade: "))
# Verifica se o usuário é maior de idade
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
    
# Questão 03

numero = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# Questão 04 

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verifica qual número é maior
if numero1 > numero2:
    print(f"O número {numero1} é o maior.")
elif numero2 > numero1:
    print(f"O número {numero2} é o maior.")
else:
    print("Os dois números são iguais.")

# Questão 05

valor_compra = float(input("Digite o valor da compra (R$): "))

# Verifica se o valor da compra é maior que R$ 100
if valor_compra > 100:
    desconto = valor_compra * 0.10  # Calcula 10% de desconto
    valor_com_desconto = valor_compra - desconto  # Aplica o desconto
    print(f"Você recebeu um desconto de R$ {desconto:.2f}.")
    print(f"O valor final da compra é R$ {valor_com_desconto:.2f}.")
else:
    print(f"O valor da compra é R$ {valor_compra:.2f}, sem desconto.")

# Questão 06 

numero = int(input("Digite um número: "))

# Verifica se o número é múltiplo de 5
if numero % 5 == 0:
    print(f"O número {numero} é múltiplo de 5.")
else:
    print(f"O número {numero} não é múltiplo de 5.")

# Questão 07

# Solicita as três notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

# Verifica se a média é maior ou igual a 7
if media >= 7:
    print(f"A média foi {media:.2f}. O aluno foi aprovado.")
else:
    print(f"A média foi {media:.2f}. O aluno foi reprovado.")

# Questão 08

# Solicita a senha ao usuário
senha = input("Digite a senha: ")

# Verifica se a senha está correta
if senha == "python123_EFG":
    print("Acesso permitido")
else:
    print("Senha incorreta")

# Questão 09 

# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Verifica se o usuário tem direito à entrada gratuita
if idade < 5 or idade > 60:
    print("Você tem direito à entrada gratuita.")
else:
    print("Você não tem direito à entrada gratuita.")

# Questão 10 

# Solicita a nota ao usuário
nota = float(input("Digite uma nota entre 0 e 10: "))

# Verifica se a nota está dentro do intervalo válido
if 0 <= nota <= 10:
    print(f"A nota informada foi: {nota}")
else:
    print("Erro! A nota deve estar entre 0 e 10.")

# Questão 11

# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Classifica o usuário com base na idade
if idade < 12:
    print("Você é uma criança.")
elif 12 <= idade <= 17:
    print("Você é um adolescente.")
else:
    print("Você é um adulto.")

# Questão 12 

# Solicita três números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Verifica qual número é o maior
maior = numero1  # Inicializa com o primeiro número

if numero2 > maior:
    maior = numero2  # Se o segundo número for maior, atualiza a variável
if numero3 > maior:
    maior = numero3  # Se o terceiro número for maior, atualiza a variável

# Exibe o maior número
print(f"O maior número é {maior}.")

# Questão 13 

# Solicita dois números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verifica se o segundo número é zero
if numero2 == 0:
    print("Erro! A divisão por zero não é possível.")
else:
    # Realiza a divisão e exibe o resultado
    resultado = numero1 / numero2
    print(f"O resultado da divisão é: {resultado:.2f}")

# Questão 14 

# Solicita um número ao usuário
numero = float(input("Digite um número: "))

# Verifica se o número está entre 10 e 50
if 10 <= numero <= 50:
    print(f"O número {numero} está entre 10 e 50.")
else:
    print(f"O número {numero} não está entre 10 e 50.")


# Questão 15

# Solicita a média do aluno
media = float(input("Digite a média do aluno: "))

# Verifica a situação do aluno com base na média
if media >= 7:
    print("Aprovado")
elif 5 <= media < 7:
    print("Em recuperação")
else:
    print("Reprovado")

# Questão 16

# Solicita o peso e a altura do usuário
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Verifica a categoria do IMC
if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}. Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print(f"Seu IMC é {imc:.2f}. Você está com peso normal.")
else:
    print(f"Seu IMC é {imc:.2f}. Você está acima do peso.")

# Questão 17 

# Solicita os três lados do triângulo
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

# Verifica se os lados podem formar um triângulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # Verifica o tipo de triângulo
    if lado1 == lado2 == lado3:
        print("O triângulo é Equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é Isósceles.")
    else:
        print("O triângulo é Escaleno.")
else:
    print("Os valores não podem formar um triângulo.")

# Questão 18 

# Solicita o nome de usuário e a senha
usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

# Verifica se o nome de usuário e a senha estão corretos
if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido!")
else:
    print("Nome de usuário ou senha incorretos.")

# Questão 19

# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Verifica se o usuário pode dirigir
if idade >= 18:
    print("Você pode dirigir!")
else:
    faltam = 18 - idade
    print(f"Você ainda não pode dirigir. Faltam {faltam} anos para poder dirigir.")


















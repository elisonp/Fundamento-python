# - Imprima uma mensagem na tela com o título de calculadora;
# - Solicite ao usuário qual o tipo de operação matemática o mesmo deseja realizar, sendo soma, subtração, divisão e multiplicação.
# Faça isso imprimindo a seguinte mensagem: "Qual o tipo de operação matemática você deseja realizar?";
# - Solicite os dois valores que serão utilizados na operação;
# - Exiba o resultado na tela.

print('Bem-vindo à calculadora')

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

operacao = input("Digite o tipo de operação(+, -, *, /): ")

if operacao == '+': produto = num1 + num2
elif operacao == '-': produto = num1 - num2
elif operacao == '*': produto = num1 * num2
elif operacao == '/': produto = num1 / num2
else:
    print("Você digitou o tipo de operação errada ou não inseriu um número antes da operação.")

print(f"O resultado da operação é: {produto}")
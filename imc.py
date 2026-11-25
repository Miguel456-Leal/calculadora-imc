
print("===== CALCULADORA DE IMC =====")

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"\nOlá, {nome}!")
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso adequado")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")

print(f"\n{nome}, obrigado por utilizar nossa calculadora!")
print("===== FIM DO PROGRAMA =====")

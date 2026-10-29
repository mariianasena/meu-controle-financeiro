
print("=== MEU CONTROLE FINANCEIRO ===")
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")
idade = input("Qual é a sua idade? ")
print("Você tem", idade, "anos")

salario = float(input("Qual é o seu salário mensal? "))
print("Seu salário mensal é R$:", salario)

alimentacao = float(input("Quanto você gastou com alimentação? R$: "))
transporte =float(input("Transporte: R$ "))
aluguel =float(input("Aluguel: R$ "))
total = alimentacao + transporte + aluguel

print(f"Total de despesas: R$ {total:.2f}")
restante = salario - total
print(f"Saldo Restante R$: {restante:.2f}")

if restante < 0:
    print("Atenção! Você gastou mais do que recebeu!")

else:
    print("Parabéns! O seu saldo não está negativo!")
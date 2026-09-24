#Calculadora de desconto
preco = float(input("Digite o preço do produto: R$ "))
percentual = float(input("Digite o percentual de desconto: "))

valor_desconto = preco * percentual / 100
preco_final = preco - valor_desconto

print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
#Calcular o Preço Final de um Pedido (com pergunta)

#valorHamburguer = float(input())
#quantidadeHamburguer = int(input())
#valorBebida = float(input())
#quantidadeBebida = int(input())
#valorPago = float(input())

# //TODO: Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).
# //TODO: Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.
# //TODO: Imprimir a saída no formato especificado neste desafio.

valorHamburguer = float(input("\nDigite o valor unitário do hambúrguer: "))
quantidadeHamburguer = int(input("Digite a quantidade de hambúrgueres: "))
valorBebida = float(input("Digite o valor unitário da bebida: "))
quantidadeBebida = int(input("Digite a quantidade de bebidas: "))
valorPago = float(input("Digite o valor pago pelo usuário: "))

valorTotalHamburguer = valorHamburguer * quantidadeHamburguer
valorTotalBebida = valorBebida * quantidadeBebida
total = float(valorTotalHamburguer + valorTotalBebida)
troco = float(valorPago - total)


print(f"\n O preço final do pedido é R$ {total:.2f}. \n Seu troco é R$ {troco:.2f}.\n")
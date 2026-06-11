
faturamentos = [12000, 8500, 4000, 15000, 6000]
bonus = 1.05

for faturamento in faturamentos:
	if faturamento > 10000:
		print("Loja Meta Atingida. Antes: ", faturamento, " depois: ", faturamento*bonus)
	else:
		print("Loja Abaixo da Meta: ", faturamento)
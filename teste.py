def verifica_fibonacci(num):
    fib1 = 0
    fib2 = 1
    while fib2 < num:
        temp = fib2
        fib2 += fib1
        fib1 = temp
    if fib2 == num:
        print(num, "pertence à sequência de Fibonacci.")
    else:
        print(num, "não pertence à sequência de Fibonacci.")
        
num = int(input("Digite um número inteiro: "))
verifica_fibonacci(num)

''''''

faturamento_diario = [

		 22174.1664
,
	
		 24537.6698
	,
	
		26139.6134
	,
	
		0.0
	,
	
		0.0
	,
	
		26742.6612
	,
	
		0.0
	,
	
		42889.2258
	,
	
		46251.174
	,
	
		11191.4722
	,
	
		0.0
	,
	
		0.0
	,
	
		3847.4823
     ,
	
		373.7838
	,
	
		2659.7563
	,
	
        48924.2448
	,
	
		18419.2614
	,
	
		0.0
	,
	
		0.0
	,
	
		35240.1826
	,
	
		43829.1667
	,
	
		18235.6852
	,
	   
        4355.0662
	,
	
		 13327.1025
	,
	
		0.0
	,
	
		0.0
	,
	
		25681.8318
	,
	
		1718.1221
	,
	
		13220.495
	,
	
		8414.61
	
]

menor_valor = min(faturamento_diario)
print("Menor valor de faturamento diário: R$", menor_valor)

maior_valor = max(faturamento_diario)
print("Maior valor de faturamento diário: R$", maior_valor)

dias_uteis = 0
for i in faturamento_diario:
    if i > 0:
        dias_uteis += 1

media_mesal = sum(faturamento_diario) / dias_uteis

dias_acima_media = sum(1 for i in faturamento_diario if i > media_mesal)
print("Número de dias com faturamento diário superior à média mensal:", dias_acima_media)


''''''


faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_faturamento = sum(faturamento.values())

for estado, valor in faturamento.items():
    percentual = (valor / total_faturamento) * 100
    print(f"{estado}: {percentual:.2f}%")

    ''''''

nome = input("Digite seu nome: ")

nome_invertido = nome[::-1]

print("Seu nome invertido é:", nome_invertido)
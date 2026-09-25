#CALCULADORA DE CONSUMO DE ENERGIA ELETRICA

print("Calculadora de consumo de energia elétrica")

nome_aparelho = input("Digite o nome do aparelho:")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
tempo_uso = float(input("digite o tempo de uso diário do aparelho em horas (h):"))

Consumo_mensal = (potencia * tempo_uso * 30) / 1000

  #Calculo de custo estimado
custo_estimado = Consumo_mensal * 0.5  # Considerando o preço do kWh como R$ 0,50

print(f"O consumo mensal do {nome_aparelho} é de {Consumo_mensal:.2f} kWh.")
print(f"O custo estimado é de R$ {custo_estimado:.2f}.")
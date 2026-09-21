# Verificador de Preços Inteligente

preco = float(input("Digite o preço do produto: R$ "))

if preco <= 100:
    print("✅ Produto com preço acessível!")
else:
    print("⚠️ Produto com preço elevado!")

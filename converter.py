def convert_currency(amount, rate):
    return amount * rate

# Função principal do programa
def main():
    print("Bem-vindo ao Conversor de Moedas!")

    # Vamos usar uma taxa fixa para conversão (por exemplo, de R$ para USD)
    rate = 0.18  # Exemplo: 1 BRL = 0.18 USD (você pode mudar para outras taxas)

    # Entrada do usuário
    amount = float(input("Digite um valor em reais (R$): "))
    
    # Realiza a conversão
    converted_amount = convert_currency(amount, rate)
    
    # Exibe o resultado
    print(f"R${amount:.2f} equivale a ${converted_amount:.2f} USD")

if __name__ == "__main__":
    main()

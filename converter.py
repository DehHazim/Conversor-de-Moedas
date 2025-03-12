def convert_currency(amount, rate):
    return amount * rate

def main():
    print("Bem-vindo ao Conversor de Moedas!")

     rate = 0.18  # Exemplo: 1 BRL = 0.18 USD (você pode mudar para outras taxas)

    amount = float(input("Digite um valor em reais (R$): "))
    
    converted_amount = convert_currency(amount, rate)
    
    print(f"R${amount:.2f} equivale a ${converted_amount:.2f} USD")

if __name__ == "__main__":
    main()

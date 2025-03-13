valor = float(input('Digite um valor em reais: R$ '))
dolar = valor / 5.81
euro = valor / 6.51
libra = valor / 7.51

print('o valor R${:.2f} corresponde aproximadamente a {:.2f} dólares, {:.2f} euros e {:.2f} libras esterlinas'.format(valor, dolar, euro, libra))

#conversão de fahrenhelt para celcius

f = float(input("Digite o valor em fahrenheit para a conversão: \n"))

c = (f - 32) / 1.8
print("F: {:.2f}°".format(f))
print("C: {:.2f}°".format(c))     

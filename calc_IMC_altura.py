sexo = input("Digite seu sexo [M | F]: ")
altura = float(input("Digite sua estatura: "))

sexo = sexo.upper() ''' variavel sexo para caixa alta,
para caixa baixa seria sexo.lower()'''

if sexo == "F":
    peso = (72.7 * altura) - 58
    print("Seu peso ideal é {:.2f} Kg".format(peso))
elif sexo == "M":
    peso = (62.1 * altura) - 44.7
    print("Seu peso ideal é {:.2f} Kg".format(peso))
else:
    print("Opção de sexo inválida.")

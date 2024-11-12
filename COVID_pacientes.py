print("COVID-19")
num_pac = int(input("Informe a quantidade de pacientes: "))

suspeitos = 0

for x in range(num_pac):
    print("Paciente: {}".format(x + 1))
    tosse = int (input("Tosse? \n.1 Sim \n.2 Não \nResp.:"))
    febre = int (input("Febre? \n.1 Sim \n.2 Não \nResp.:"))
    resp = int (input("Dif. Respiracao? \n.1 Sim \n.2 Não \nResp.:"))

    if tosse == 1 and febre == 1 and resp == 1:
        suspeitos += 1

print("Suspeitos de COVID - 19: {}".format(suspeitos))

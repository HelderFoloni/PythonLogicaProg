#comentário em única linha

#inteiro
idade = 20
#python pode mudar o tipo da variável em tempo de execução
print (type(idade))
idade = 17.5

#ponto flutuante
estatura = 1.82
#string (caractere)
saudacao = "Olá"
#logicá (booleana)
aprovado = True

print (type(idade))
print (type(estatura))
print (type(saudacao))
print (type(aprovado))

'''comentário em várias linhas'''

'''
1 O SENHOR reina; está vestido de majestade. O SENHOR se revestiu e cingiu de poder; o mundo também está firmado, e não poderá vacilar.
2 O teu trono está firme desde então; tu és desde a eternidade.
3 Os rios levantam, ó Senhor, os rios levantam o seu ruído, os rios levantam as suas ondas.
4 Mas o Senhor nas alturas é mais poderoso do que o ruído das grandes águas e do que as grandes ondas do mar.
5 Mui fiéis são os teus testemunhos; a santidade convém à tua casa, Senhor, para sempre.
'''
print("concatenação")
numero1 = input("Digite o primeiro numero: ") #recebe como caractere pois nao foi feita a conversão
numero2 = input("Digite o segundo numero: ")

print(numero1)
print(numero2)


soma = numero1 + numero2 #não fez a soma, ao invés concatenou dois strings
print("Concatenação = {}".format(soma))

print("soma")
numero1 = int(input("Digite o primeiro numero: ")) #faz a conversão para inteiro
numero2 = int(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

soma = numero1 + numero2 #realiza a soma pois os dados são inteiros pois foram cnvertidos
dobro = numero3 * 2 #realiza a operação de dobro, já que houve a conversão
print("Soma = {}".format(soma))
print("Dobro = {:.2f}".format(dobro))


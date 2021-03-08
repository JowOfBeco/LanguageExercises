enderecoClient= {"rua": "Avenida periquito Roxo", "numero": 51, "referencia": "Ao lado do posto dos irmãos"} ##Declaração de dict
#
#
print("Vamos receber seus dados:\n") ##entrada de dados
pesoAltura = [float(input("Peso\n")), float(input("altura\n"))]##conversão para float
calcIMC = pesoAltura[0] / (pesoAltura[1] * pesoAltura[1])
valida = int(input("Gostaria de verificar seu IMC? Digite 1 pra sim ou 0 para nao.\n"))#digitar exatamente como no código
#a cima conversão e uso de boolean
#
if valida == True and calcIMC< 18.5:
	print(f" Seu imc é {calcIMC}, você está bem Magrinho, vamos agendar sua consulta agora !\n")
	day = input("dia\n")
	month = input("mes\n")
	print(f"Sua consulta ficou marcada para dia{day}/{month} ")
elif calcIMC < 25:
	print(f" Seu imc é {calcIMC}, você está normal, continuamos no plano.\n")
elif calcIMC < 30:
	print(f" Seu imc é {calcIMC}, você está bem Pesadinho, mas ainda está tranquilo. \n")
elif calcIMC > 30:
	print(f" Seu imc é {calcIMC}, você está em obesidade, alerta! VAMOS AGENDAR SUA CONSULTA AGORA !!\n")
	day = int(input("dia\n")) # conversão de numero para inteiro
	month = int(input("mes\n")) #conversão de numero para inteiro
	print(f"Sua consulta ficou marcada para dia{day}/{month}\n")
else: print("Perfeito. \n")
lista = ["Johmself Santos Pereira", "Masculino","Brasileiro"]
tupla=(enderecoClient,lista, "Mãe : Rosenilde" ) #declaração tupla

print("Confira seu endereço:\n", enderecoClient, "\nConfira dados pessoais:\n", lista,f"Primeiro nome da sua começa começa com:\n>>>{tupla[2][6]}<<<?\n")
resposta = input("ok? ou nao?\n")
if resposta == "ok":
	print("Fique com Deus!\n")
else :print("Consultar secretária para reajuste de cadastro!")


#This code will receive an user input and after get its range and sum consecutive numbers

N = int(input())
resultado = 0

for var in range(N+1):
    resultado = resultado + var

print(resultado)

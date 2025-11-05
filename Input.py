

num = int(input("Escriba el limite: "))

for i in range(num):
    for k in range(i): 
        if k % 2 == 0:
            print("la pocision es par")
        else:
            print("la posicion es impar")


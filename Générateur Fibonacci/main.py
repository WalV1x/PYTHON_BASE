numbers = int(input("Entrez le nombre de nombres à afficher : "))

a = 0
b = 1
total = 0

print("Les {0} premiers nombres de la suite Fibonacci sont :".format(numbers), end = " ")
for i in range(numbers):
    print(total, end = " ")
    total = a + b
    a = b
    b = total
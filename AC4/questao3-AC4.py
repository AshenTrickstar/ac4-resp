n = 1
a = 0
b = 0
c = 0
d = 0

while n > 0:
    n = int(input("Informe um número: "))
    if n >= 0 and n <= 25:
        a = a + 1
    elif n >= 26 and n <= 50:
        b = b + 1
    elif n >= 51 and n <= 75:
        c = c + 1
    elif n >= 76 and n <= 100:
        d = d + 1

print("A quantia de números entre 0 e 25 é: ", a, " entre 26-50 é: ", b, " entre 51-75 é: ", c, " entre 76-100 é: ", d)
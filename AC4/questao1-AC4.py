def e_primo(num):
    primo = True

    for div in range(2, num):
        if num % div == 0:
            print(div)
            primo = False

    if primo == True:
        print("É primo")
    else:
        print("Não é primo")
        
e_primo(42)
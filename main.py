def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return  "impar"

numero = int(input("Digite um número inteiro: "))
print(f'O número {numero} é {par_ou_impar(numero)}.')

#20/10/2023
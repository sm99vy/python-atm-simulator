notas = 0
cedula = 50

print('Olá, bem-vindo ao banco ! Notas disponíveis: R$ 50,00 | R$ 20,00 | R$ 10,00 | R$ 1,00')
valor_saque = int(input('Digite o valor que deseja sacar: R$'))
total = valor_saque

while True:
    if total >= cedula:
        total -= cedula
        notas += 1
    else:
        if notas > 0:
            print(f'Total de {notas} cédulas de R${cedula} !')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        notas = 0
        if total == 0:
            break
print('Volte sempre :)')
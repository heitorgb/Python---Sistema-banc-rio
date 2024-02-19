menu = '''
######################## MENU #########################

    [d] para Depositar
    [s] para Sacar
    [e] para Extrato
    [i] para Sair

 ------------- 
'''

saldo = 500
limite = 500
extrato = ''
numero_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = int(input('Informe o valor a ser depositado: '))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'Deposito R$ {valor_deposito:.2f}\n'

        else:
            print('Valor deve ser maior que zero.')

    elif opcao == 's':
        if numero_saques < LIMITE_DE_SAQUES:
            if saldo > 0: 
                valor_saque = int(input('Informe o valor a ser sacado: '))
                if valor_saque > 0:
                    saldo -= valor_saque 
                    numero_saques += 1
                    print('Saque efeituado com sucesso!')
                    extrato += f'Saque R$ {valor_saque:.2f}'
                else:
                    print('O valor de saque não pode ser menor que zero. ')
            else:
                print('Saldo insuficiente!')        
        else: 
            print('Número de saques diários excedido.')        

    elif opcao == 'e':
        print('\n################ EXTRATO #################')
        print('Não foram realizadas movimentações.'if not extrato else extrato)
        print(f'\nSaldo R$ {saldo:.2f}')
        print('############################################')
        
    elif opcao == 'i':
        print('Obrigado por usar nossos serviços!')   
        break        

    else:
        print('opção inválida, por favor, escolha uma opção válida')

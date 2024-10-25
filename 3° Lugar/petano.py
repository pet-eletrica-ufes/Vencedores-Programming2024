import random

times = ['Flamengo', 'Vasco', 'Fluminense', 'Botafogo', 'Atlético mg', 'Bahia']
saldo = 0
cupom = ('pet2024')


     
while True:
    print('BEM VINDO AO PETANO\nINSIRA UM COMANDO NUMÉRICO DE 1 A 6\nCOMANDO 1 DEPÓSITO\nCOMANDO 2 SAQUE\nCOMANDO 3 SALDO\nCOMANDO 4 CUPOM\nCOMANDO 5 CONFRONTO\nCOMANDO 6 SAIR')
    comando = int(input('Comando: '))
    
    
    if comando not in range (1,7): # validar o comando
         comando = int(input('Comando inválido \n Digite outro comando.'))

    else:
            if comando == 1:                  #comando
                valor = float(input('Valor a ser depositado:'))
                saldo += valor 
                print(f'Novo saldo:R${saldo}')

            elif comando == 2:
                valor = float(input('Valor a ser sacado:'))  
                while valor >= saldo:
                    print('Saldo insuficiente.\n Digite outro valor')
                    valor = float(input('valor a ser sacado'))
            
                saldo -= valor
                print (f"O valor foi sacado \n o seu saldo atual é de : {saldo}")
            
            elif comando == 3:
                print (f'Saldo atual:R${saldo}')

            elif comando == 4:
                cupom_inserido = str(input('Digite o cupom:'))
                if cupom_inserido == cupom:
                    saldo += 100
                    print('Parabéns R$ 100,00 foi depositado em sua conta')
                else:
                    print("Cupom inválido")
            
            elif comando == 5:
                random.shuffle(times)
                confrontos = []
                for i in range(0, 6 , 2):
                    confrontos.append((times[i], times[i + 1]))
                for i, confronto in enumerate(confrontos, start=1):
                    print(f'Confronto {i}: {confronto[0]} vs {confronto[1]}\n ')
                confronto_escolhido = int(input('Escolha um confronto: ')) - 1
                
                if confronto_escolhido not in range (0,4):      
                        print ('Número inválido\n Digite um número de 1 a 3') 
                        confronto_escolhido = int(input('Escolha um confronto: ')) - 1
                else:
                    
                        time_escolhido = input('Escolha um time: ')
                    
                        valor_apostado = int(input('Qual o valor que você quer apostar?'))

                if valor_apostado <= saldo:

                                vencedor = random.choice(confrontos[confronto_escolhido])
                                print (f'O vencedor do confronto {confronto_escolhido + 1 } é: {vencedor}')

                else :
                                
                                print('Saldo insuficiente')            
                if (time_escolhido.upper() == vencedor.upper()):
                            saldo += valor_apostado * 2
                            print(f'Parabéns o time escolhido venceu\n o seu saldo atual é de R${saldo}')
                else : 
                                saldo -= valor_apostado
                                print(f'O time escolhido perdeu\n Seu saldo atual é de R${saldo}')       
            elif comando == 6:
                   print('Fechando..')
                   break
                                
                    


                    


                
                
            



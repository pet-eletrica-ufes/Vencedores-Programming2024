import random
from colorama import Fore, Style



times = ['atletico mineiro', 'flamengo', 'corinthians', 'botafogo', 'vasco', 'internacional', 'palmeiras', 'santos', 'sao paulo', 'fluminense']
resultados = {1: ('Flamengo', 'Vasco'),
              2: ('Internacional', 'Corinthians',),
              3: ('Atlético Mineiro', 'Botafogo',),
              4: ('Palmeiras', 'Santos'),
              5: ('São Paulo', 'Fluminense'),}
saldo = 0
historico = []

print()
print(Fore.LIGHTMAGENTA_EX +  "BEM-VINDO À PLATAFORMA MEGbet⚡\n"
      "- como podemos ajudar? -" + Style.RESET_ALL)
print()


while True:

    print(Fore.LIGHTWHITE_EX + '══════ ⋆ ★ ⋆ ═══════ \n'
          '1. 💸 Depositar\n2. 🤑 Sacar\n3. 💵 Saldo\n4. 🎰 Apostar\n5. 📝 Histórico de apostas\n6. 🏁 Sair\n' \
          '══════ ⋆ ★ ⋆ ═══════ \n'+ Style.RESET_ALL)

    comando = int(input(Fore.LIGHTMAGENTA_EX +'Escolha uma opção: '+ Style.RESET_ALL))
    print()

    if comando == 1: #deposito
        deposito = float(input(Fore.CYAN +"valor a ser depositado: "+ Style.RESET_ALL))
        saldo+=deposito
        print()
        

    elif comando == 2:  # saque
        
        if saldo == 0:  # Verifica se o saldo é zero antes de pedir o saque
            print(f"Você deve ter dinheiro em sua conta para realizar o saque.")
        else:
            saque = float(input(Fore.CYAN + 'saque: ' + Style.RESET_ALL))

            if saque > saldo:
                print(Fore.LIGHTRED_EX + f' Operação inválida! Seu saque deverá ser menor que: {saldo}' + Style.RESET_ALL)
            else:
                saldo -= saque  # Atualiza o saldo subtraindo o valor do saque
                print(f'Saque realizado! Valor do saque: {saque}')

    
    if comando == 3: #saldo
        print(Fore.CYAN + f"\nSeu saldo atual é: R${saldo}" + Style.RESET_ALL)
        print()

    if comando == 4: #aposta
        print(Fore.LIGHTBLUE_EX + "Esses são os jogos disponíveis:\n"
              "1. Flamengo x Vasco\n"
              "2. Internacional x Corinthians\n"
              "3. Atlético Mineiro x Botafogo\n"
              "4. Palmeiras x Santos\n" 
              "5. São Paulo x Fluminense\n" + Style.RESET_ALL)


        Jogo = int(input('Qual jogo deseja apostar?: '))
        print()

        if Jogo in resultados:
            time1, time2 = resultados[Jogo]
            print(f"Você escolheu apostar no jogo: {time1} x {time2} ✅ ")
            print()

            time_apostado = input(f"Escolha um time para apostar ({time1} ou {time2}): ")
            print()

            if time_apostado == time1 or time_apostado == time2:

                valor_aposta = float(input("Digite o valor da aposta: "))

                if valor_aposta > saldo:
                    print(Fore.LIGHTRED_EX + "Saldo insuficiente para essa aposta."+ Style.RESET_ALL)


                elif valor_aposta <= 0:
                    print(Fore.LIGHTRED_EX + "O valor da aposta deve ser positivo.")

                else:
                    saldo -= valor_aposta  # Deduz a aposta do saldo
                    print(f"Aposta de R$ {valor_aposta} registrada para o time {time_apostado}.")
                    print()
                    # Simula o resultado do jogo
                    resultado = random.choice ([time1, time2])  # Um dos dois times vence aleatoriamente
                    print(f"O resultado do jogo é: {resultado} venceu! 🏆 ")

                    if resultado == time_apostado:
                        premio = valor_aposta *2
                        print(f"Parabéns! Você ganhou! Seu prêmio é: R$ {premio} 🏆")
                        saldo += valor_aposta *2  # Dobra a aposta se o time vencer
                        print("==============")

                    else:
                        print(Fore.LIGHTRED_EX + " ☹ você perdeu a aposta."+ Style.RESET_ALL)
                        print()

                    print(f"Seu saldo atual é R$ {saldo}")
                    print()

                    historico.append(f"Jogo: {time1} x {time2}\n"
                    f"Aposta: {time_apostado}\n"
                    f"Resultado: {resultado}\n"
                    f"Valor da aposta:R$ {valor_aposta}\n"
                    f"Valor ganho: R$ {valor_aposta *2 if resultado == time_apostado else 0}\n"
                    f"Valor perdido: R$ {valor_aposta if resultado != time_apostado else 0}")
                print()

            else:
                print(Fore.LIGHTRED_EX + "Time inválido para aposta."+ Style.RESET_ALL)

        else:
                print(Fore.LIGHTRED_EX + "Jogo inválido."+ Style.RESET_ALL)


    elif comando == 5:
                print(Fore.CYAN + "Historico de apostas:\n" + Style.RESET_ALL)
                if historico:
                    for aposta in historico:
                        print(aposta)
                        print()
                else:
                    print("Nenhuma aposta feita")
                    print()

    elif comando == 6:  # sair
            print(Fore.LIGHTBLACK_EX+ "Saindo... Obrigado por jogar! 🏁"+ Style.RESET_ALL)

            break

    if comando >=7: 
            print (Fore.LIGHTRED_EX + "Ops, tente novamente ⚠ Escolha de 1 à 6!!" + Style.RESET_ALL)
           

   
#a bet da cracolandia

import random

def exibir_eventos(eventos):
    print("Eventos disponíveis para aposta:")
    for i, evento in enumerate(eventos):
        print(f"{i + 1}. {evento['nome']} (Odds: {evento['odds']})")

def gerar_eventos_aleatorios(esporte, jogo=None):
    times = {
        "futebol": [
            "Flamídia", "Palmerda", "São Pica", "Corinthians", "Atlético Mineiro", "Grêmio", "Internacional",
            "Flubixa", "Vascaicai", "Botafogo", "Ceará",
            "Bahia", "Athletico Paranaense", "Fortaleza", "Cruzeiro"
        ],
        "volei": [
            "SESC RJ", "Minas", "Osasco", "Rio do Sul",
            "São Paulo/Barueri", "Curitiba", "Fluminense", "Bauru"
        ],
        "basquete": [
            "Flamerda", "São Paulo", "Paulistano", "Pinheiros",
            "Franca", "Caxias do Sul", "Mogi, menino lobo", "Fortaleza"
        ],
        "esports": {
            "Lol": ["Team Liquid", "SK Telecom T1", "G2 Esports", "Fnatic"],
            "Overwatch": ["Overwatch League", "New York Excelsior", "Los Angeles Gladiators"],
            "Fifa": ["Fifa E-World Cup", "Team Vitality", "FC Schalke 04"],
            "Valorant": ["Sentinels", "G2 Esports", "FaZe Clan"],
            "Fortnite": ["Ninja", "Tfue", "Flakes Power", "Lwkolrick", "Clebito"]
        }
    }

    eventos = []
    if esporte == "esports":
        for _ in range(3):
            time1 = random.choice(times[esporte][jogo])
            time2 = random.choice([time for time in times[esporte][jogo] if time != time1])
            evento = {
                "nome": f"{time1} vs {time2}",
                "odds": round(random.uniform(1.5, 3.0), 2),
                "time1": time1,
                "time2": time2
            }
            if evento not in eventos:
                eventos.append(evento)
    else:
        while len(eventos) < 3:
            time1 = random.choice(times[esporte])
            time2 = random.choice([time for time in times[esporte] if time != time1])
            evento = {
                "nome": f"{time1} vs {time2}",
                "odds": round(random.uniform(1.5, 3.0), 2),
                "time1": time1,
                "time2": time2
            }
            if evento not in eventos:
                eventos.append(evento)

    return eventos

def realizar_aposta():
    print("================================================================================\n")   
    print("Bem-vindo ao Bethanos!")
    print("Com apenas um estalar de dedos, seu dinheiro cai pela metade!\n")
    print("Programa feito por: Companhia Garotos de Programa.\n")
    print("================================================================================\n")
    print("Antes de você perder seu dinheiro, por favor, passe suas informações.\n")
    
    saldo = round(random.uniform(1, 1000), 2)
    
    nome = input("Digite seu nome: ")
    
    print(f"{nome}! Aqui estão algumas informações sobre a Bethanos:\n ")
    print("1. Você pode apostar em esportes tradicionais.")
    print("2. Também oferecemos apostas em eSports para nerdolas.")
    print("3. As odds indicam o multiplicador do seu ganho em caso de vitória.")
    print("4. Você pode depositar e sacar valores para gerenciar seu saldo.")
    print("5. Esse programa é apenas para maiores de 18 anos.\n")
    print("Lembre-se: apostas não são pra diversão, então me dê todo o seu dinheiro!\n")
    
    while True:
        idade = input("Digite sua idade: ")
        
        if not idade.isdigit():
            print("Idade inválida. Digite uma idade válida. Tente novamente!")
            continue
        
        idade = int(idade)

        if idade < 18:
            print("Você precisa ter pelo menos 18 anos para fazer apostas.")
            print("(Na próxima vez seja inteligente e digite uma idade superior a 18)")
            return

        break

    print(f"\nBem-vindo de volta, {nome}! Seu saldo é de R$ {saldo:.2f}\n.")

    while True:
        print("Escolha uma opção:")
        print("1. Aposta")
        print("2. Saldo")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Sair")

        opcao = input("Digite o número da opção desejada ou 'v' para voltar: ")

        if opcao == '1':
            while True:
                tipo_esporte = input("Você deseja apostar em (1) Esportes tradicionais ou (2) eSports para nerdolas? (ou 'v' para voltar): ")
                if tipo_esporte == 'v':
                    break
                if tipo_esporte not in ['1', '2']:
                    print("Escolha 1 ou 2, burro(a).")
                    continue

                if tipo_esporte == '1':
                    esporte = input("Escolha um esporte: ").strip().lower()
                    if esporte not in ["futebol", "volei", "basquete"]:
                        print("Infelizmente esse tipo de esporte não é valorizado o suficiente para as pessoas apostarem nele, por favor, escolha algum do catálogo.")
                        continue
                else:
                    esporte = "esports"
                    jogo = input("Qual jogo você deseja apostar? (Lol, Overwatch, Fifa, Valorant, Fortnite) (ou 'v' para voltar): ").strip().title()
                    if jogo == 'v':
                        break
                    if jogo not in ["Lol", "Overwatch", "Fifa", "Valorant", "Fortnite"]:
                        print("Jogo inválido! Tente novamente.")
                        continue

                eventos = gerar_eventos_aleatorios(esporte, jogo if tipo_esporte == '2' else None)
                exibir_eventos(eventos)

                while eventos and saldo > 0:
                    escolha = input("Escolha o evento (número) ou 'v' para voltar: ")
                    if escolha.lower() == 'v':
                        break
                    escolha = int(escolha) - 1
                    if escolha < 0 or escolha >= len(eventos):
                        print("Evento inválido!")
                        continue

                    time1 = eventos[escolha]['time1']
                    time2 = eventos[escolha]['time2']
                    print(f"Escolha o time para apostar:")
                    print(f"1. {time1}")
                    print(f"2. {time2}")

                    escolha_time = input("Digite 1 ou 2 (ou 'v' para voltar): ").strip()
                    if escolha_time == 'v':
                        break
                    if escolha_time not in ['1', '2']:
                        print("Escolha inválida! Você deve digitar 1 ou 2.")
                        continue
                    
                    time_escolhido = time1 if escolha_time == '1' else time2

                    valor_aposta = input(f"Digite o valor da aposta: R$ (Saldo disponível: R$ {saldo:.2f}) (ou 'v' para voltar): ")
                    if valor_aposta == 'v':
                        break
                    valor_aposta = float(valor_aposta)

                    if valor_aposta > saldo:
                        print("Você não tem dinheiro pra isso, pobre.")
                        continue

                    resultado = random.choice([True, False])  
                    if resultado:
                        ganho = valor_aposta * eventos[escolha]['odds']
                        saldo += ganho
                        print(f"Parabéns, {nome}! Infelizmente você ganhou R$ {ganho:.2f}! Seu novo saldo é R$ {saldo:.2f}.")
                    else:
                        saldo -= valor_aposta
                        print(f"Felizmente, {nome}, você perdeu a aposta. Seu saldo agora é de R$ {saldo:.2f}.")

                    eventos.pop(escolha)

                    if saldo <= 0:
                        print("Sua grana acabou! Obrigado pelo seu dinheiro!")
                        break

        elif opcao == '2':
            print(f"Seu saldo atual é: R$ {saldo:.2f}")

        elif opcao == '3':
            while True:
                deposito = input("Digite o valor do depósito: R$ (ou 'v' para voltar): ")
                if deposito == 'v':
                    break
                try:
                    deposito = float(deposito)
                    if deposito <= 0:
                        print("Como que tu bota isso cara, faz o negócio certo dessa vez.")
                        continue
                    saldo += deposito
                    print(f"Depósito realizado com sucesso! Seu novo saldo é R$ {saldo:.2f}")
                    break
                except ValueError:
                    print("Por favor, insira um valor válido.")

        elif opcao == '4':
            while True:
                saque = input("Digite o valor do saque: R$ (ou 'v' para voltar): ")
                if saque == 'v':
                    break
                try:
                    saque = float(saque)
                    if saque > saldo:
                        print("Você nem tem dinheiro suficiente para fazer esse saque.")
                        continue
                    saldo -= saque
                    print(f"Saque realizado com sucesso! Seu novo saldo é R$ {saldo:.2f}")
                    break
                except ValueError:
                    print("Por favor, insira um valor válido.")

        elif opcao == '5':
            print("Obrigado por jogar! Até a próxima!")
            break

        elif opcao.lower() == 'v':
            continue  # Retorna ao menu principal

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    realizar_aposta()

import os

# Inicializa a lista de dados
dados = []

# Inicializa contadores
total_familias = len(dados)
total_salario = 0
total_filhos = 0

# Calcula os totais iniciais
for salario, filhos in dados:
    total_salario += salario
    total_filhos += filhos

# Loop do menu
while True:
    print("\nMenu:")
    print("1 - Adicionar família")
    print("2 - Exibir resultados")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        # Adiciona nova família
        salario = float(input("Salário da família: "))
        filhos = int(input("Número de filhos: "))
        dados.append((salario, filhos))
        
        # Atualiza contadores
        total_familias += 1
        total_salario += salario
        total_filhos += filhos

    elif opcao == '2':
        # Exibe os resultados
        if total_familias > 0:
            media_salario = total_salario / total_familias
            media_filhos = total_filhos / total_familias
            
            # Encontra o maior e menor salário
            maior_salario = dados[0][0]
            menor_salario = dados[0][0]
            for salario, _ in dados:
                if salario > maior_salario:
                    maior_salario = salario
                if salario < menor_salario:
                    menor_salario = salario

            # Mostra os resultados
            print(f"Total de famílias: {total_familias}")
            print(f"Média do salário: R$ {media_salario:.2f}")
            print(f"Média de filhos: {media_filhos:.2f}")
            print(f"Maior salário: R$ {maior_salario:.2f}")
            print(f"Menor salário: R$ {menor_salario:.2f}")
        else:
            print("Nenhuma família cadastrada.")

    elif opcao == '3':
        # Encerra o programa
        break

    else:
        print("Opção inválida. Tente novamente.")

import os
from dataclasses import dataclass, asdict

@dataclass
class Familia:
    salario: float
    filhos: int

# Inicializa a lista de dados
dados = []

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
        nova_familia = Familia(salario, filhos)
        dados.append(nova_familia)
        
        # Salva dados no arquivo
        with open("pesquisa_prefeitura.txt", "w") as file:
            for familia in dados:
                file.write(f"{familia.salario},{familia.filhos}\n")

    elif opcao == '2':
        # Exibe os resultados
        total_familias = len(dados)
        total_salario = sum(familia.salario for familia in dados)
        total_filhos = sum(familia.filhos for familia in dados)

        if total_familias > 0:
            media_salario = total_salario / total_familias
            media_filhos = total_filhos / total_familias
            
            # Encontra o maior e menor salário
            maior_salario = max(familia.salario for familia in dados)
            menor_salario = min(familia.salario for familia in dados)

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

import os
os.system("cls || clear")
from dataclasses import dataclass

@dataclass
class Familia:
    salario: float
    filhos: int
# Lista de dados.
dados = []

# Um comando para ter um laço de repetição.
while True:
    print("\nMenu:")
    print("1 - Adicionar família")
    print("2 - Exibir resultados")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")

# Condição para adicionar novas familias.
    if opcao == '1':
        os.system("cls || clear")
        salario = float(input("Salário da família: "))
        filhos = int(input("Número de filhos: "))
        nova_familia = Familia(salario, filhos)
        dados.append(nova_familia)
        
        # Salvar dados no arquivo.
        with open("pesquisa_prefeitura.txt", "w") as file:
            for familia in dados:
                file.write(f"{familia.salario},{familia.filhos}\n")

    elif opcao == '2':
        os.system("cls || clear")
        # Calculando dados.
        total_familias = len(dados)
        total_salario = sum(familia.salario for familia in dados)
        total_filhos = sum(familia.filhos for familia in dados)
        
        if total_familias > 0:
            media_salario = total_salario / total_familias
            media_filhos = total_filhos / total_familias
            
            # Encontra o maior e o menor salario.
            maior_salario = max(familia.salario for familia in dados)
            menor_salario = min(familia.salario for familia in dados)

            # Exibindo resultados.
            print(f"Quantidade de famílias: {total_familias}")
            print(f"Média salarial: R$ {media_salario:.2f}")
            print(f"Média de filhos: {media_filhos:.2f}")
            print(f"Maior salário: R$ {maior_salario:.2f}")
            print(f"Menor salário: R$ {menor_salario:.2f}")
        else:
            print("Insira dados de uma familia.")

    elif opcao == '3':
        break
    else:
        print("Errou. Tente novamente mais tarde. ")

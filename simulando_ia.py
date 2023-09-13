import csv
import random


# Gerando dados para simular o comportamento de uma IA.
def generate_random_age_list(num_ages, min_age=1, max_age=100):
    """Gera uma lista de idades aleatórias."""
    age_list = [random.randint(min_age, max_age) for _ in range(num_ages)]
    return age_list

# Salva os arquivos para futuralmente serem extraídos (ETL)
def save_age_list_to_csv(age_list, filename):
    """Salva a lista de idades em um arquivo CSV."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Idade"])  # Escreve o cabeçalho
        for age in age_list:
            writer.writerow([age])

def main():
    num_ages = int(input("Quantas idades você gostaria de gerar e salvar em um arquivo CSV? "))

    if num_ages <= 0:
        print("Número inválido de idades. Por favor, insira um número positivo.")
        return

    age_list = generate_random_age_list(num_ages)
    csv_filename = "idades.csv"

    save_age_list_to_csv(age_list, csv_filename)

    print(f"As idades geradas foram salvas no arquivo '{csv_filename}'.")

if __name__ == "__main__":
    main()

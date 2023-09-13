import pandas as pd

# Extract [E]TC
def extract_ages_from_csv(csv_filename):
    """Extrai idades de um arquivo CSV usando Pandas."""
    try:
        df = pd.read_csv(csv_filename)
        ages = df["Idade"].tolist()
        return ages
    except FileNotFoundError:
        print(f"O arquivo '{csv_filename}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")
        return []

def main():
    csv_filename = "idades.csv"
    age_list = extract_ages_from_csv(csv_filename)

    if not age_list:
        return

    print("As idades extraídas do arquivo CSV são:")
    for age in age_list:
        print(age)

    average_age = sum(age_list) / len(age_list)
    print(f"A média das idades é: {average_age:.2f}")

if __name__ == "__main__":
    main()

import pandas as pd

# Extract [E]TL
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

# Na fase de T extraímos os dados do arquivo .csv - mas não tivemos uma transformação de fato, deixo a cargo dos próxmos passos nesse projeto;

# L ET[L]
def explain_mean(ages):
    """Explica o conceito de média ao usuário."""
    if not ages:
        print("Não há idades disponíveis para calcular a média.")
        return

    total = sum(ages)
    count = len(ages)
    mean = total / count

    print("O que é Média?")
    print("A média é uma medida estatística que representa o valor típico de um conjunto de números.")
    print(f"No nosso caso, temos um conjunto de idades com {count} valores.")
    print(f"A soma de todas essas idades é {total}.")
    print(f"A média é calculada dividindo a soma pelo número de idades: {total} / {count} = {mean:.2f}")
    print(f"Portanto, a média das idades é {mean:.2f}.")

def main():
    csv_filename = "idades.csv"
    age_list = extract_ages_from_csv(csv_filename)

    if not age_list:
        return

    print("As idades extraídas do arquivo CSV são:")
    for age in age_list:
        print(age)

    # average_age = sum(age_list) / len(age_list)
    # print(f"A média das idades é: {average_age:.2f}")

    explain_mean(age_list)

if __name__ == "__main__":
    main()

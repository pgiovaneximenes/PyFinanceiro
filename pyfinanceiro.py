"""
PyFinanceiro - Análise de registros financeiros
Lê dados_financeiros.csv e gera relatório com métricas financeiras.
"""

import csv
import os


def carregar_dados(caminho_csv):
    """Lê o CSV e retorna listas de datas e valores."""
    datas = []
    valores = []
    with open(caminho_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            datas.append(row["Data"].strip())
            valores.append(int(row["Lucros/Perdas"].strip()))
    return datas, valores


def analisar(datas, valores):
    """Calcula todas as métricas financeiras."""
    total_meses = len(valores)
    total = sum(valores)
    media = total / total_meses

    # Variações mês a mês
    variacoes = [valores[i] - valores[i - 1] for i in range(1, len(valores))]
    variacao_media = sum(variacoes) / len(variacoes) if variacoes else 0

    # Maior aumento e maior redução
    max_aumento_val = max(variacoes)
    max_aumento_data = datas[variacoes.index(max_aumento_val) + 1]

    max_reducao_val = min(variacoes)
    max_reducao_data = datas[variacoes.index(max_reducao_val) + 1]

    return {
        "total_meses": total_meses,
        "total": total,
        "media": media,
        "variacao_media": variacao_media,
        "maior_aumento": (max_aumento_data, max_aumento_val),
        "maior_reducao": (max_reducao_data, max_reducao_val),
    }


def formatar_relatorio(resultado):
    """Formata os resultados como string de relatório."""
    linhas = [
        "Analise Financeira",
        "----------------------------",
        f"Total de meses: {resultado['total_meses']}",
        f"Total: $ {resultado['total']}",
        f"Média: $ {resultado['media']:.2f}",
        f"Variação da média: $ {resultado['variacao_media']:.2f}",
        f"Maior aumento nos lucros: {resultado['maior_aumento'][0]} ($ {resultado['maior_aumento'][1]})",
        f"Maior redução nos lucros: {resultado['maior_reducao'][0]} ($ {resultado['maior_reducao'][1]})",
    ]
    return "\n".join(linhas)


def main():
    caminho_csv = os.path.join(os.path.dirname(__file__), "dados_financeiros.csv")

    if not os.path.exists(caminho_csv):
        print(f"Erro: arquivo '{caminho_csv}' não encontrado.")
        print("Coloque o arquivo dados_financeiros.csv na mesma pasta do script.")
        return

    datas, valores = carregar_dados(caminho_csv)
    resultado = analisar(datas, valores)
    relatorio = formatar_relatorio(resultado)

    # Imprime no terminal
    print(relatorio)

    # Exporta relatorio.txt na mesma pasta do script
    caminho_txt = os.path.join(os.path.dirname(__file__), "relatorio.txt")
    with open(caminho_txt, "w", encoding="utf-8") as f:
        f.write(relatorio + "\n")

    print(f"\nRelatório exportado: {caminho_txt}")


if __name__ == "__main__":
    main()

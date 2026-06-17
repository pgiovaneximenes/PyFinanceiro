# 💸 PyFinanceiro

Script Python para análise de registros financeiros a partir de um arquivo CSV. Calcula métricas financeiras e exporta um relatório em texto.

## 📊 Funcionalidades

- Total de meses no período analisado
- Valor total líquido de Lucros/Perdas
- Média mensal de Lucros/Perdas
- Variação média mês a mês
- Maior aumento nos lucros (data e valor)
- Maior redução nos lucros (data e valor)

## 📁 Estrutura do projeto

```
PyFinanceiro/
├── pyfinanceiro.py        # Script principal
├── dados_financeiros.csv  # Dados de entrada
└── relatorio.txt          # Relatório gerado (criado ao executar)
```

## ▶️ Como usar

**Pré-requisito:** Python 3.x instalado.

1. Clone o repositório:
   ```bash
   git clone https://github.com/pgiovaneximenes/PyFinanceiro.git
   cd PyFinanceiro
   ```

2. Coloque o arquivo `dados_financeiros.csv` na pasta do projeto.  
   O CSV deve ter duas colunas separadas por vírgula:
   ```
   Data,Lucros/Perdas
   Jan-2010,867884
   Feb-2010,-69417
   ...
   ```

3. Execute o script:
   ```bash
   python pyfinanceiro.py
   ```

## 📋 Exemplo de saída

```
Analise Financeira
----------------------------
Total de meses: 86
Total: $ 38382578
Média: $ 446309.05
Variação da média: $ -2315.12
Maior aumento nos lucros: Feb-2012 ($ 1926159)
Maior redução nos lucros: Sep-2013 ($ -2196167)
```

O relatório também é exportado automaticamente para `relatorio.txt` na mesma pasta.

## 🛠️ Tecnologias

- Python 3
- Módulos da biblioteca padrão: `csv`, `os` (sem dependências externas)

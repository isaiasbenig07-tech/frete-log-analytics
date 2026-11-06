#!/usr/bin/env python3
"""
Módulo de Análise Financeira e Gestão de Fretes para Transportadoras.
Calcula custos operacionais, repasses a terceiros, combustível e margem líquida.
"""

import pandas as pd

def processar_dados_transportadora(caminho_csv):
    # Carrega os dados operacionais
    df = pd.read_csv(caminho_csv)

    # Cálculos operacionais e financeiros
    df['custo_total'] = df['pagamento_terceiros'] + df['combustivel'] + df['outros_custos']
    df['lucro_liquido'] = df['faturamento'] - df['custo_total']
    df['margem_lucro_%'] = (df['lucro_liquido'] / df['faturamento']) * 100

    print("=== RELATÓRIO FINANCEIRO DE FRETES (2026) ===")
    print(df[['mes', 'faturamento', 'custo_total', 'lucro_liquido', 'margem_lucro_%']].to_string(index=False))

    # Consolidação dos totais
    faturamento_total = df['faturamento'].sum()
    terceiros_total = df['pagamento_terceiros'].sum()
    combustivel_total = df['combustivel'].sum()
    lucro_total = df['lucro_liquido'].sum()
    margem_media = (lucro_total / faturamento_total) * 100

    print("\n=== RESUMO EXECUTIVO DO ANO ===")
    print(f"Faturamento Total:       R$ {faturamento_total:,.2f}")
    print(f"Pago a Terceiros:        R$ {terceiros_total:,.2f} ({(terceiros_total/faturamento_total)*100:.1f}% do Faturamento)")
    print(f"Gastos com Combustível:   R$ {combustivel_total:,.2f} ({(combustivel_total/faturamento_total)*100:.1f}% do Faturamento)")
    print(f"Lucro Líquido Acumulado: R$ {lucro_total:,.2f}")
    print(f"Margem Líquida Média:    {margem_media:.2f}%")

if __name__ == "__main__":
    processar_dados_transportadora('../data/fretes_2026.csv')

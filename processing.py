# criando medidas:
def calcular_medidas(emendas):
    global total_por_uf_bi, total_por_funcao_bi, total_pago_por_ano_bi, gap_empenhado_e_pago

    total_por_uf = emendas.groupby(emendas["UF"]).sum(numeric_only=True).round(2)
    total_por_uf_bi = total_por_uf / 1000000000 # total gasto por bilhao

    total_por_funcao = emendas.groupby(emendas["Nome Função"]).sum(numeric_only=True).round(2)
    total_por_funcao_bi = total_por_funcao / 1000000000 # total gasto por bilhao

    total_por_ano = emendas.groupby(emendas["Ano da Emenda"]).sum(numeric_only=True).round(2)
    total_por_ano_bi = total_por_ano / 1000000000 # total gasto por bilhao
    total_por_ano_bi = total_por_ano_bi.reset_index() # transformando o index em uma coluna

    gap_empenhado_e_pago = total_por_uf_bi[["Valor Empenhado", "Valor Pago"]]

calcular_medidas()
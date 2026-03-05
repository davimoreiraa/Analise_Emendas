import cleaning as clean
import visualization as visu

emendas = clean.carregar_e_limpar()
visu.top_10_eficientes(emendas)
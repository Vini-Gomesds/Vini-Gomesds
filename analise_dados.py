import pandas as pd

# Caminho para o arquivo Excel
base_rh = r'C:\Users\vgome\Documents\Trabalho\Gestao de Carreira\Portfólio\GitHub e Python\Base_RH_Python.xlsx'

# Carregar a planilha
df = pd.read_excel(base_rh)
print(df.head())

print("Script iniciado com sucesso!")

import os
import pandas as pd

# Descobre a pasta onde está o script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Monta o caminho até o arquivo CSV
csv_path = os.path.join(base_dir, '..', 'data', 'Walmart_Sales.csv')

# Lê o arquivo CSV usando o caminho correto
df = pd.read_csv(csv_path)

# Verifica valores nulos
df.isnull().sum()


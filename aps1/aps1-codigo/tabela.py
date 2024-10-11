import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ler o arquivo CSV
df = pd.read_csv('tabela.csv')

# Criar uma figura e eixos
fig, ax = plt.subplots(figsize=(12, 8))

# Remover eixos
ax.axis('off')

# Criar a tabela
table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')

# Ajustar o layout da tabela
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.2, 1.2)

# Ajustar o espaçamento entre as células
table.auto_set_column_width(col=list(range(len(df.columns))))

# Adicionar cores alternadas às linhas para melhor legibilidade
for i in range(len(df)):
    for j in range(len(df.columns)):
        cell = table[i + 1, j]
        if i % 2 == 0:
            cell.set_facecolor('#f0f0f0')
        else:
            cell.set_facecolor('#ffffff')

# Adicionar um título

# Salvar a imagem
plt.savefig('search_algorithms_table.png', dpi=1000, bbox_inches='tight')

print("A tabela foi salva como 'search_algorithms_table.png'")
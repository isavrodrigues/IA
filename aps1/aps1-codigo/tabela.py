import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('tabela.csv')
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')

table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')

table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.2, 1.2)

table.auto_set_column_width(col=list(range(len(df.columns))))

for i in range(len(df)):
    for j in range(len(df.columns)):
        cell = table[i + 1, j]
        if i % 2 == 0:
            cell.set_facecolor('#f0f0f0')
        else:
            cell.set_facecolor('#ffffff')

plt.savefig('search_algorithms_table.png', dpi=1000, bbox_inches='tight')

print("A tabela foi salva como 'search_algorithms_table.png'")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tabela.csv')

df['Tempo de processamento em segundos'] = pd.to_numeric(df['Tempo de processamento em segundos'], errors='coerce').fillna(0)

algorithms = df['Agoritimo'].unique()

plt.figure(figsize=(12, 6))

for algorithm in algorithms:
    data = df[df['Agoritimo'] == algorithm]
    plt.plot(data['Objetivo'], data['Tempo de processamento em segundos'], label=algorithm)

plt.xlabel('Objetivo')
plt.ylabel('Tempo de processamento (segundos)')
plt.title('Comparação de Desempenho dos Algoritmos de Busca')
plt.legend()
plt.yscale('log') 
plt.grid(True)
plt.savefig('search_algorithms_comparison.png')
plt.close()

print("O gráfico foi salvo como 'search_algorithms_comparison.png'")

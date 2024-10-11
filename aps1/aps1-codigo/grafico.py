import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('tabela.csv')

# Convert 'Tempo de processamento em segundos' to numeric, replacing 'NaN' with 0
df['Tempo de processamento em segundos'] = pd.to_numeric(df['Tempo de processamento em segundos'], errors='coerce').fillna(0)

# Create a list of unique algorithms
algorithms = df['Agoritimo'].unique()

# Create the plot
plt.figure(figsize=(12, 6))

for algorithm in algorithms:
    data = df[df['Agoritimo'] == algorithm]
    plt.plot(data['Objetivo'], data['Tempo de processamento em segundos'], label=algorithm)

plt.xlabel('Objetivo')
plt.ylabel('Tempo de processamento (segundos)')
plt.title('Comparação de Desempenho dos Algoritmos de Busca')
plt.legend()
plt.yscale('log')  # Use logarithmic scale for y-axis due to large range of values
plt.grid(True)

# Save the plot as a PNG file
plt.savefig('search_algorithms_comparison.png')
plt.close()

print("O gráfico foi salvo como 'search_algorithms_comparison.png'")
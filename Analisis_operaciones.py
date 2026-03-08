import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar los datos
df = pd.read_csv('operaciones_tecnologicas.csv')

# 2. Configuración estética de las gráficas
sns.set_theme(style="whitegrid")

# 3. Gráfica 1: Costo Total por Categoría (Impacto Financiero)
plt.figure(figsize=(10, 6))
costo_cat = df.groupby('Categoria')['Costo_Operativo'].sum().sort_values(ascending=False)
sns.barplot(x=costo_cat.index, y=costo_cat.values, palette='magma')
plt.title('Inversión Operativa Total por Categoría de Ticket', fontsize=14)
plt.ylabel('Costo Total (USD)')
plt.xlabel('Categoría')
plt.savefig('costo_por_categoria.png') # Se guarda la imagen para GitHub
plt.close()

# 4. Gráfica 2: Tiempo de Resolución por Prioridad (Eficiencia)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Prioridad', y='Tiempo_Resolucion_Min', data=df, 
            order=['Baja', 'Media', 'Alta', 'Crítica'], palette='viridis')
plt.title('Distribución de Tiempos de Resolución según Prioridad', fontsize=14)
plt.ylabel('Tiempo (Minutos)')
plt.savefig('tiempos_prioridad.png')
plt.close()

print("Análisis finalizado. Se han generado los archivos: costo_por_categoria.png y tiempos_prioridad.png")
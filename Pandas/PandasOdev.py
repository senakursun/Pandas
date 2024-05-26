import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# 1. Rastgele x ve y koordinatlarını oluşturma
num_points = 1000
x_coords = np.random.randint(0, 1001, num_points)
y_coords = np.random.randint(0, 1001, num_points)

# 2. Koordinatları bir DataFrame'e kaydetme
df = pd.DataFrame({'x': x_coords, 'y': y_coords})

# 3. DataFrame'i bir Excel dosyasına kaydetme
excel_path = 'coordinates.xlsx'
df.to_excel(excel_path, index=False)

# 4. Excel dosyasından koordinatları okuma
df = pd.read_excel(excel_path)

# 5. Koordinatları görselleştirme
fig, ax = plt.subplots()
grid_size = 200  
num_colors = (1000 // grid_size) + 1
colors = list(mcolors.TABLEAU_COLORS.values())[:num_colors]

# Izgara boyutlarını ayarlama
x_grid = 1000 // grid_size
y_grid = 1000 // grid_size

# Her ızgaradaki noktaları farklı renklerde gösterme
color_index = 0
for i in range(0, 1000, grid_size):
    for j in range(0, 1000, grid_size):
        mask = (df['x'] >= i) & (df['x'] < i + grid_size) & (df['y'] >= j) & (df['y'] < j + grid_size)
        ax.scatter(df[mask]['x'], df[mask]['y'], color=colors[color_index % len(colors)])
        color_index += 1

# Grafik ayarları
plt.title('Rastgele Koordinatların Görselleştirilmesi')
plt.xlabel('X Koordinatları')
plt.ylabel('Y Koordinatları')
plt.grid(True)
plt.show()

# Grafiği kaydetme
plt.savefig('coordinates_visualization.jpeg')
plt.show()

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Load clean data
file_path = "/storage/emulated/0/Lesson/nigeria-dashboard/Data/nigeria_gdp_clean.csv"
nigeria = pd.read_csv(file_path, index_col='Year')

# --- Chart 1: GDP Growth Over Time (Line Chart) ---
plt.figure(figsize=(12, 5))
plt.plot(nigeria.index, nigeria['GDP_Growth'], color='green', linewidth=2)
plt.axhline(y=0, color='red', linestyle='--', linewidth=1)
plt.title("Nigeria GDP Growth Rate (1961–2024)", fontsize=16)
plt.xlabel("Year")
plt.ylabel("GDP Growth (%)")
plt.xticks(nigeria.index[::5], rotation=45)
plt.tight_layout()
plt.savefig("/storage/emulated/0/Lesson/nigeria-dashboard/Data/chart1_line.png", dpi=150)
plt.close()
print("✅ Chart 1 saved!")

# --- Chart 2: Top 10 Best & Worst Years (Bar Chart) ---
top10 = nigeria.nlargest(10, 'GDP_Growth')
bottom10 = nigeria.nsmallest(10, 'GDP_Growth')
combined = pd.concat([top10, bottom10]).sort_values('GDP_Growth')

colors = ['red' if x < 0 else 'green' for x in combined['GDP_Growth']]

plt.figure(figsize=(12, 6))
plt.barh(combined.index.astype(str), combined['GDP_Growth'], color=colors)
plt.axvline(x=0, color='black', linewidth=0.8)
plt.title("Nigeria: Top 10 Best & Worst GDP Growth Years", fontsize=14)
plt.xlabel("GDP Growth (%)")
plt.tight_layout()
plt.savefig("/storage/emulated/0/Lesson/nigeria-dashboard/Data/chart2_bar.png", dpi=150)
plt.close()
print("✅ Chart 2 saved!")

print("\n🎉 All charts saved to your Data folder!")
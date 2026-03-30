import pandas as pd

# Dosya yollarını tırnak içinde tam yazalım
input_path = r'C:\Users\pc\Desktop\full_dataset_1000(Sheet1).csv'
output_path = r'C:\Users\pc\Desktop\infinitesignal.csv'

df = pd.read_csv(input_path)
df.columns = [c.lower().replace(' ', '_') for c in df.columns]
df.to_csv(output_path, index=False)

print("Sinyal temizlendi! Masaüstüne 'infinitesignal.csv' olarak geldi. 💅")
import pandas as pd
import os

print("=== ЗАГРУЗКА ДАННЫХ ===")
print("Текущая папка:", os.getcwd())
print("Файлы в папке:", os.listdir('.'))

# Загружаем с абсолютным путём
file_path = '/Users/maximvishnevskiy/ml_practice_7/transactions_diy.csv'
df = pd.read_csv(file_path)

print(f"\nФайл загружен: {len(df)} строк")
print(f"Колонки: {list(df.columns)}")
print(f"\nПервые 3 строки:")
print(df.head(3))

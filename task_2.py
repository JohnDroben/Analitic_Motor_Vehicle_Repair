# Определите среднюю зарплату (Salary) по городу (City)
# - используйте файл приложенный к дз - dz.csv

import pandas as pd

df = pd.read_csv('dz.csv', sep=',')
print(f"средняя зарплата по городу", df.groupby('City')['Salary'].mean())       # средняя зарплата по городу
print(f"максимальная зарплата по городу", df.groupby('City')['Salary'].max())       # максимальная зарплата по городу
print(f"минимальная зарплата по городу", df.groupby('City')['Salary'].min())       # минимальная зарплата по городу

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Имя': ['Алексей', 'Борис', 'Виктор', 'Галина', 'Дмитрий', 'Екатерина', 'Иван', 'Лариса', 'Мария', 'Николай'],
    'Математика': [100, 78, 92, 88, 74, 95, 68, 81, 20, 84],
    'Физика': [79, 85, 90, 86, 80, 92, 70, 83, 75, 88],
    'Химия': [82, 88, 91, 89, 76, 93, 72, 85, 78, 87],
    'Биология': [84, 10, 88, 91, 79, 94, 71, 86, 74, 89],
    'История': [81, 80, 87, 90, 78, 92, 69, 84, 76, 86]
}

df = pd.DataFrame(data)
print(df.head(10))

# Средняя оценка по каждому предмету
mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

# Медианная оценка по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print("\nQ1 и Q3 для оценок по математике:")
print("Q1 (Первый квартиль):", Q1_math)
print("Q3 (Третий квартиль):", Q3_math)


# IQR для оценок по математике
IQR_math = Q3_math - Q1_math
print("\nIQR для оценок по математике:", IQR_math)

# Cтандартное отклонение для оценок по каждому предмету
std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)

# Визуализация первоначальных данных по математике
plt.figure(figsize=(10, 6))
df.boxplot(column=['Математика'])
plt.title('Boxplot для оценок по математике (первоначальные данные)')
plt.show()

# Определяем нижнюю и верхнюю границы для определения выбросов
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

lower_bound = Q1_math - 1.5 * IQR_math
upper_bound = Q3_math + 1.5 * IQR_math

print("Q1 (25-й перцентиль):", Q1_math)
print("Q3 (75-й перцентиль):", Q3_math)
print("IQR (межквартильный размах):", IQR_math)
print("Нижняя граница для выбросов:", lower_bound)
print("Верхняя граница для выбросов:", upper_bound)

# Удаляем выбросы
df_no_outliers = df[(df['Математика'] >= lower_bound) & (df['Математика'] <= upper_bound)]

# Визуализация данных после удаления выбросов
plt.figure(figsize=(10, 6))
df_no_outliers.boxplot(column=['Математика'])
plt.title('Boxplot для оценок по математике (без выбросов)')
plt.show()

# Вывод нового DataFrame
print("\nНовый DataFrame без выбросов:")
print(df_no_outliers)


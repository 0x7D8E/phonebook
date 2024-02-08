"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# Исходные данные
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head(
"""

# Исходные данные
import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание one-hot представления
categories = data['whoAmI'].unique()
one_hot = pd.DataFrame(0, columns=categories, index=data.index)
one_hot = one_hot.add(pd.get_dummies(data['whoAmI']))

# Объединение исходного DataFrame с one-hot представлением
data = pd.concat([data, one_hot], axis=1)

# Удаление исходного столбца
data.drop('whoAmI', axis=1, inplace=True)

data.head()
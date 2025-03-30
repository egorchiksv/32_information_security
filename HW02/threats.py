import pandas as pd
import numpy as np
df = pd.read_excel('./threats.xlsx')
list1 = df['Меры защиты'].str
df2 = pd.DataFrame(columns=['Код меры защиты', 'Наименование меры защиты', 'Количество баллов'])
list2 = []
for i in list1.split('\n'):
    for j in i:
        list2.append(j)

dict_ = {}
list3 = []
for i in set(list2):
    temp = list()
    dict_[i] = list2.count(i)
    temp.insert(0, i[:i.find(' ')])
    temp.insert(1, i[i.find(' ') + 1:])
    temp.insert(2, list2.count(i))
    df2.loc[len(df2.index)] = [temp[0], temp[1], temp[2]]
print(df2)
df2.sort_values(ascending=False, by='Количество баллов').to_excel('./threats_result.xlsx')
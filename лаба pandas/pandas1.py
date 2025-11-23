import pandas as pd

df = pd.read_csv('transactions.csv')
df['SUM'] = pd.to_numeric(df['SUM'])

#Задача1: 3 самых крупных платежа из реально проведённых (статус OK)
ok_data = df[df['STATUS'] == 'OK']
top_3 = ok_data.nlargest(3, 'SUM')
print("Топ-3 платежа со статусом OK:")
print(top_3[['CONTRACTOR', 'SUM']])
print()

#Задача2: определите полную сумму реально проведённых платежей в адрес Umbrella, Inc.
umbrella_ok = df[(df['CONTRACTOR'] == 'Umbrella, Inc') & (df['STATUS'] == 'OK')]
total = umbrella_ok['SUM'].sum()
print("Сумма платежей Umbrella, Inc со статусом OK:")
print(total)
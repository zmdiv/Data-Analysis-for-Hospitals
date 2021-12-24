import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 14)

general = pd.read_csv("test/general.csv")
prenatal = pd.read_csv("test/prenatal.csv")
sports = pd.read_csv("test/sports.csv")

prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

united = pd.concat([general, prenatal, sports], ignore_index=True)
united.drop(columns=['Unnamed: 0'], inplace=True)

united.dropna(how='all', inplace=True)
united['gender'].replace({'female': 'f', 'woman': 'f', 'man': 'm', 'male': 'm', }, inplace=True)
united['gender'].fillna('f', inplace=True)
united.fillna({'bmi': 0, 'diagnosis': 0, 'blood_test': 0, 'ecg': 0, 'ultrasound': 0,
               'mri': 0, 'xray': 0, 'children': 0, 'months': 0}, inplace=True)

# ANSWERS FOR THE PREVIOUS STAGE
q1 = united.hospital.mode()[0]
q2 = round((united.loc[united['hospital'] == 'general', 'diagnosis']).value_counts()['stomach'] / len(
    (united.loc[united['hospital'] == 'general', 'diagnosis'])), 3)
q3 = round((united.loc[united['hospital'] == 'sports', 'diagnosis']).value_counts()['dislocation'] / len(
    (united.loc[united['hospital'] == 'sports', 'diagnosis'])), 3)
q4 = int(united.loc[united['hospital'] == 'general', 'age'].median() - (
    united.loc[united['hospital'] == 'sports', 'age'].median()))
q5_1 = united.loc[united['blood_test'] == 't', 'hospital'].mode()[0]
q5_2 = united.loc[united['hospital'] == q5_1, 'blood_test'].count()

print(f'The answer to the 1st question is {q1}')
print(f'The answer to the 2nd question is {q2}')
print(f'The answer to the 3rd question is {q3}')
print(f'The answer to the 4th question is {q4}')
print(f'The answer to the 5th question is {q5_1}, {q5_2}  blood tests')

gr1 = 0  # 0-15
gr2 = 0  # 15-35
gr3 = 0  # 35-55
gr4 = 0  # 55-70
gr5 = 0  # 70-80

gr1k = '0-15'  # 0-15
gr2k = '15-35'  # 15-35
gr3k = '35-55'  # 35-55
gr4k = '55-70'  # 55-70
gr5k = '70-80'  # 70-80

for age in united.age:
    if age < 15:
        gr1 += 1
    elif 15 <= age < 35:
        gr2 += 1
    elif 35 <= age < 55:
        gr3 += 1
    elif 55 <= age < 70:
        gr4 += 1
    else:
        gr5 += 1

gr_dict = {gr1k: gr1, gr2k: gr2, gr3k: gr3, gr4k: gr4, gr5k: gr5}
united.plot(y='age', kind='hist', bins=10)
plt.show()
print(f'The answer to the 1st question: {max(gr_dict, key=gr_dict.get)}')
united.diagnosis.value_counts().plot(kind='pie')
plt.show()
print(f'The answer to the 2nd question: {united.diagnosis.mode()[0]}')
sns.violinplot(x='height', y='hospital', data=united)
plt.show()
print("The answer to the 3rd question: It's because...")

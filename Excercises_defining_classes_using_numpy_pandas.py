import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Part A.1
df = pd.read_excel('FLU09_data.xlsx', sheet_name='FLU09 plasma', index_col=0)

# Part A.2
df.rename(columns={'log_VL': 'log_Viral_load'}, inplace=True)

# Part A.3
df.loc[3211, 'log_Viral_load'] = 2
df.loc[3213, 'log_Viral_load'] = 2
df.loc[3263, 'log_Viral_load'] = 2
df.loc[3393, 'log_Viral_load'] = 2

# Part A.4
df['Viral_load'] = np.exp(10 * df['log_Viral_load'])

# Part A.5
viral_load_max = df['Viral_load'].max()

df['Viral_load'] = df['Viral_load'] / viral_load_max

# Part A.6
df.drop(index=3208, inplace=True)


# Part A.7
def addsub(indexstr):
    ''' adds 'sub_' to a string.'''
    return 'sub_' + indexstr


index_names = df.index.tolist()
index_names = list(map(str, index_names))
index_names = list(map(addsub, index_names))

df['sub'] = index_names
df.set_index('sub', inplace=True)

# Part A.8
neg_flu_list = df[df['Flu_positive'] == False]
flu_neg_logVL_average = neg_flu_list['log_Viral_load'].mean()

# Part A.9
maximal_mean = df.mean(axis=0, numeric_only=True).max()

# Part A.10
num_subjects_A_ph1 = sum(df['Strain'] == 'A (pH1)')

# Part A.11
subjects_A_H3_mean_IL8 = df[df['Strain'] == 'A (H3)'].IL8.mean()

# Part A.12
df_flu = df[df['Flu_positive'] == True]

# Part A.13
df_flu = df_flu[df_flu['Strain'] != 'B']

# Part A.14
df_flu_gender = df_flu.value_counts('Gender')

# Part A.15
df_flu_females = df_flu_gender.loc['Female'] / df_flu_gender.sum() * 100


# Part B
plt.figure()
sns.boxplot(x=df_flu.Strain[(df_flu['Strain'] == 'A (pH1)') | (df_flu['Strain'] == 'A (H3)')], y=df_flu.log_Viral_load, hue=df_flu.Gender)
plt.savefig('strain_and_gender.jpg', dpi=300)
plt.show()

# Part C


class patient09:
    def __init__(self, database_row):
        '''define class called patient that recieves a row from the patient database.'''
        self.age = database_row[0]
        self.gender = database_row[1]
        self.positive = database_row[2]
        self.cytokine_val_list = [database_row[6:26]]

    def cytokine_mean_score(self):
        '''function returns the mean of all the cytokines values.'''
        score = np.nansum(self.cytokine_val_list)
        return score

    def __eq__(self, other):
        '''equals operator compares gender and flu_positive of 2 patients and returns true if both are equal.'''
        if self.gender == other.gender:
            if self.positive == other.positive:
                return True
        return False


df = pd.read_excel('FLU09_data.xlsx', sheet_name='FLU09 plasma', index_col=0)

patient3206 = patient09(df.loc[3206])
patient3357 = patient09(df.loc[3357])

eq_q = patient3357 == patient3206
mean_3206 = patient3206.cytokine_mean_score()
mean_3357 = patient3357.cytokine_mean_score()

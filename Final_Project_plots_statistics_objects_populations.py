
import scipy.stats
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import random
from scipy.stats import ttest_ind
import math

folder_path = 'C:/Users/97254/PycharmProjects/pythonProjectNo1/'
os.makedirs(folder_path + 'figures/', exist_ok=True)


# Part 1
# Part 1.1
def fitness_evl(x, y):
    ''' function takes x and y, assuming values between -4.5 and 4.5 and will return a z coordinate for the function: '''
    z = (x**2 + y - 11)**2 + (x + y**2 - 7)**2
    return z

# Part 1.2


class Individual:
    def __init__(self, coord_tuple):  # piazza question specifically states 'receives tuple of coordinates'
        self.x = coord_tuple[0]
        self.y = coord_tuple[1]
        self.coordinates = coord_tuple
        self.fitness = self.cal_fitness()

    def mate(self, par2):
        '''creates an offspring from two individuals'''
        gp1 = [self.x, self.y]
        gp2 = [par2.x, par2.y]
        offspring = [0, 0]
        rand_num = random.random()

        if rand_num < 0.45:
            offspring = gp1
            offspring[0] += round(random.uniform(-0.1, 0.1), 6)
            offspring[1] += round(random.uniform(-0.1, 0.1), 6)

        if 0.45 <= rand_num <= 0.8:
            offspring = gp2
            offspring[0] += round(random.uniform(-0.1, 0.1), 6)
            offspring[1] += round(random.uniform(-0.1, 0.1), 6)

        if rand_num > 0.8:
            offspring[0] += round(random.uniform(-4.5, 4.5), 6)
            offspring[1] += round(random.uniform(-4.5, 4.5), 6)

        return Individual((offspring[0], offspring[1]))

    def cal_fitness(self):
        '''calculates fitness based on the fitness_evl function'''
        return fitness_evl(self.x, self.y)


# Part 1.3


def sort_population(population):
    '''take in a list containing all individuals in the population. This function will return a new list sorted by the Individual's fitness, using insertion_sort function'''
    sorted_population = population.copy()

    for i in range(len(sorted_population)):
        key = sorted_population[i]
        j = i - 1

        while j >= 0 and key.cal_fitness() < sorted_population[j].cal_fitness():
            sorted_population[j + 1] = sorted_population[j]
            j -= 1

        sorted_population[j + 1] = key

    return sorted_population


# part 1.4

def initialize_pop(n):
    '''creates n individuals and puts them into a list.'''
    population_list = []

    for i in range(n):
        individual = Individual((round(random.uniform(-4.5, 4.5), 6), round(random.uniform(-4.5, 4.5), 6)))
        population_list += [individual]

    return population_list


list_pop = initialize_pop(30)

# Part 1.5


def main_loop(list_pop, gen_num=100, top_fit=10):
    '''The function will return a dictionary where the keys will be the numbers 1,50,100, and the values will be the list of all the individuals in that generation.'''

    result = {1: [], 50: [], 100: []}
    new_population = sort_population(list_pop.copy())

    for i in range(gen_num):  # loop for the number of generations inputted

        new_population = sort_population(new_population)
        temp_pop_list = []  # Reinitialize temp_pop_list for each generation

        for j in range(top_fit):  # first 'top_fit' number of the sorted population is added to the new generation
            temp_pop_list.append(new_population[j])

        for j in range(30 - top_fit):
            daddy = random.randint(0, top_fit)  # Random index for selecting daddy
            mommy = random.randint(0, top_fit)  # Random index for selecting mommy
            individual = new_population[daddy].mate(new_population[mommy])  # Create offspring using mate() method
            temp_pop_list.append(individual)

        new_population = temp_pop_list

        if i+1 in result.keys():
            result[i+1] = new_population

    return result


res = main_loop(list_pop)

# Part 1.6

last_pop = sort_population(res[100])
min_point = last_pop[0].cal_fitness()

# Part 1.7


x_vec_1 = []
y_vec_1 = []
x_vec_50 = []
y_vec_50 = []
x_vec_100 = []
y_vec_100 = []
for j in range(len(res[1])):
    x_vec_1 += [res[1][j].x]
    y_vec_1 += [res[1][j].y]
    x_vec_50 += [res[50][j].x]
    y_vec_50 += [res[50][j].y]
    x_vec_100 += [res[100][j].x]
    y_vec_100 += [res[100][j].y]


def himmelblau(x, y):
    ''' function takes x and y, assuming values between -4.5 and 4.5 and will return a z coordinate for the function: '''
    z = (x**2 + y - 11)**2 + (x + y**2 - 7)**2
    return z


plt.figure()
X, Y = np.meshgrid(np.linspace(-4.5, 4.5, 256), np.linspace(-4.5, 4.5, 256))
Z = himmelblau(X, Y)
levels = np.linspace(Z.min(), Z.max(), 30)
plt.title('generation number 1')
plt.xlabel('x coordinates')
plt.ylabel('y coordinates')
plt.contourf(X, Y, Z, cmap="inferno", levels=levels)
plt.scatter(x_vec_1, y_vec_1, c='g', s=15)
plt.savefig(folder_path + 'figures/gen_1.jpg', dpi=300)
plt.show()
plt.close('all')

plt.figure()
X, Y = np.meshgrid(np.linspace(-4.5, 4.5, 256), np.linspace(-4.5, 4.5, 256))
Z = himmelblau(X, Y)
levels = np.linspace(Z.min(), Z.max(), 30)
plt.title('generation number 50')
plt.xlabel('x coordinates')
plt.ylabel('y coordinates')
plt.contourf(X, Y, Z, cmap="inferno", levels=levels)
plt.scatter(x_vec_50, y_vec_50, c='g', s=15)
plt.savefig(folder_path + 'figures/gen_50.jpg', dpi=300)
plt.show()
plt.close('all')

plt.figure()
X, Y = np.meshgrid(np.linspace(-4.5, 4.5, 256), np.linspace(-4.5, 4.5, 256))
Z = himmelblau(X, Y)
levels = np.linspace(Z.min(), Z.max(), 30)
plt.title('generation number 100')
plt.xlabel('x coordinates')
plt.ylabel('y coordinates')
plt.contourf(X, Y, Z, cmap="inferno", levels=levels)
plt.scatter(x_vec_100, y_vec_100, c='g', s=15)
plt.savefig(folder_path + 'figures/gen_100.jpg', dpi=300)
plt.show()
plt.close('all')

# Part 2

# Part 2.1
df = pd.read_csv('rat_KD.txt', sep='\t')

# Part 2.2
df.set_index('row.names', inplace=True)

# Part 2.3
control_list = list(df.keys()[:6])
experimental_list = list(df.keys()[6:])

# Part 2.4


def ttest_rat(row_df):
    '''takes one row of a dataframe, separates into two lists: control and experiment and runs a Welch’s t-Test on the two sublists. returns the p-value'''
    control_rats = row_df[:6]
    experimental_rats = row_df[6:]

    pval = ttest_ind(control_rats, experimental_rats, equal_var=False)[1]

    return pval


# Part 2.5
raw_p_value = df.apply(ttest_rat, axis=1)

# Part 2.6
plt.hist(raw_p_value, bins=20)
plt.title('Raw p-value scores')
plt.xlabel('p-value')
plt.ylabel('Number of occurrences')
plt.savefig(folder_path + 'figures/p_val.jpg', dpi=300)
plt.show()

# Part 2.7
df_log2 = df.applymap(math.log2)

# Part 2.8
control_mean = df_log2.iloc[:, :6].mean(axis=1)
test_mean = df_log2.iloc[:, 6:].mean(axis=1)
df2 = pd.DataFrame({'control group mean': control_mean, 'test group mean': test_mean})

# Part 2.9
foldchange = df2['control group mean'] - df2['test group mean']

# Part 2.10
plt.hist(foldchange, bins=30)
plt.title('foldchange scores')
plt.xlabel('')
plt.ylabel('scores')
plt.savefig(folder_path + 'figures/fold_change.jpg', dpi=300)
plt.show()
plt.close('all')

# Part 2.11
df_volcano = pd.DataFrame(foldchange, columns=['foldchange'])
df_volcano['raw_p_value'] = raw_p_value


def logfunct(x):
    '''applies the -1*math.log(x) to an input'''
    return -1*math.log(x)


df_volcano['logpvalue'] = df_volcano['raw_p_value'].apply(logfunct)


# part 2.12
def is_sig(value):
    '''returns true is value is smaller than 0.1. returns false if larger than or equal to 0.1.'''
    if value < 0.1:
        return True
    return False



df_volcano['is significant'] = df_volcano['raw_p_value'].apply(is_sig)

# Part 2.13
sns.scatterplot(data=df_volcano, x='foldchange', y='logpvalue', hue='is significant')
plt.title('Foldchange scores vs p values')
plt.xlabel('fold change')
plt.ylabel('log p values')
plt.savefig(folder_path + 'figures/volcano.jpg', dpi=300)
plt.show()
plt.close('all')

# Part 2.14
values_to_keep = (df_volcano.foldchange >= 2) | (df_volcano.foldchange <= -2)
df_log2_dropped = df_log2[values_to_keep]

# Part 2.15

gene_clustermap = sns.clustermap(df_log2_dropped)
gene_clustermap.ax_heatmap.set_title('log2 values of genes with foldchange >2 or <-2')
gene_clustermap.ax_heatmap.set_xlabel('Rat Groups')
gene_clustermap.ax_heatmap.set_ylabel('Genes')
plt.tight_layout()
plt.savefig(folder_path + 'figures/gene_clustermap.jpg', dpi=300)
plt.show()

# Part 3
# Part 3.1

df_cancer = pd.read_excel('dataR2.xlsx')

# Part 3.2

df_cancer.rename(columns={'Classification': 'Cancer'}, inplace=True)

# Part 3.3

df_cancer['Cancer'].replace({1: False, 2: True}, inplace=True)

# Part 3.4

correlations = df_cancer.corr(method='spearman')
correlations_graph = sns.heatmap(correlations, vmin=-1, vmax=1, cmap='RdBu_r')
plt.title('Correlation heatmap')
plt.tight_layout()
plt.savefig(folder_path + 'figures/correlations.jpg', dpi=300)
plt.show()
plt.close('all')

# Part 3.5
glucose_cancer_true = df_cancer[df_cancer.Cancer]
glucose_cancer_false = df_cancer[df_cancer.Cancer == 0]

plt.figure()
sns.boxplot(data=df_cancer, x='Cancer', y='Glucose')
sns.stripplot(data=[glucose_cancer_false.Glucose, glucose_cancer_true.Glucose], color='black')
plt.title('Glucose levels of Cancer vs Healthy patients')
plt.savefig(folder_path + 'figures/glucose_vs_cancer.jpg', dpi=300)
plt.show()
plt.close('all')

# Part 3.6

sns.lmplot(data=df_cancer, y='MCP.1', x='Resistin', hue='Cancer')
plt.title('scatter plot with linear regression: MCP.1 vs. Resistin')
plt.tight_layout()
plt.savefig(folder_path + 'figures/correlated_vars.jpg', dpi=300)
plt.show()
plt.close('all')

spear_corr, p_value = scipy.stats.spearmanr(df_cancer['MCP.1'], df_cancer['Resistin'])
# print("Spearman correlation:", spear_corr)
# print("P-value:", p_value)
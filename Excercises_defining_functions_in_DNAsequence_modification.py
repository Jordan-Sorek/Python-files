from functools import reduce

# part A

# input: camel_list is a list of camels. first item is camel name, second is temp in C.

# temp camel list for testing
camel_list1 = [['cml_1', 38.5], ['cml_2', 36.9], ['cml_3', 39.3], ['cml_3', 35.8]]
camel1 = ['cml_1234', 38.5]


def display_camel_temp(camel):
    '''function 'display_camel_temp' receives input from a list of 2 items representing the camel name and body temperature.
    the function prints the camel name and temperature to console.'''
    print('Catalog name:', camel[0])
    print('Temperature:', camel[1])
    return


# testing function
# display_camel_temp(camel_list[1])

def C_to_F_camel(camel):
    '''this function receives input as a camel and returns its temperature value in Fahrenheit.'''
    C = camel[1]
    F = (9 / 5) * C + 32
    return F


def get_camel_temp_fahr(camel):
    '''gets a single camel (list of name and temperature in Celsius) and returns its temperature in Fahrenheit too.'''
    # find location in camel name of underscore - after which is the camel number.
    underscore_index = camel[0].index('_')
    # defines a variable for the camel number without the camel name.
    camel_number = camel[0][underscore_index + 1:]

    print('Camel number', camel_number, '-', camel[1], 'Celsius,', C_to_F_camel(camel), 'Fahrenheit')
    return


# testing function
# get_camel_temp_fahr(camel1)

def add(x, y):
    '''recieves two values, and returns sum.'''
    return x + y


def camels_list_fahr(camel_list):
    '''function that gets a list of camels (list of lists) and returns a list of their temperatures in Fahrenheit
    also prints the sum of temperatures (in Fahrenheit) of all camels.'''

    # list of temps in fahr
    fahr_list = list(map(C_to_F_camel, camel_list))

    # sum of temps in fahrenheit
    sum_fahr = reduce(add, fahr_list)
    print('Temperatures in Fahrenheit summed:', sum_fahr)

    return fahr_list


# Part B

# Part B question 1

# a list of strings named inserts, which contains the five sequences from the fasta file
#final sequences
inserts = ['GGCTATATAGCGCGATGCTGATCGCGCGCGATGCTAGCTGCTCCGCGCGCGAAT',
           'TGAATAGAATTATATAGAATGACGCGCGATGAATCCGCTACGCGATAAGTCCGTAA',
           'ACCGCGCTATATAGCGTAAGCTGAATCGCCGCGCGTAAGCTGAATCGCTAGGGGCCGCC',
           'TGGTATATACGCGCGCGCCCGCGAATGCTGATCGCCTCGCGCGTAAGATGC',
           'CCGTGAATGCCTCGTATATACGCGCTGAATGCCTGCCGCGCGCGCGCGCGCG']

# temp sequence for testing
#seq_list1 = ['ATCGGG', 'GACGATCGC', 'CGATCGTGTA']

def G_indexer(sequence):
    '''function receives a sequence and returns the index of the first 'G' character.'''
    return sequence.index('G')

# Part B question 2

def seq_list_G_index(seq_list):
    '''gets a list of strings and returns a list of integers representing the index of the first ’G’ character in each string.'''
    #this line creates a list 'G_index_list', and uses 'map' to perform function 'G_indexer' on the input 'seq_list'.
    G_index_list = list(map(G_indexer, seq_list))
    return G_index_list

#Apply the seqs_G_index(seq_list) function on inserts and assign the output list to new variable named inserts_G_indices.
inserts_G_indices = seq_list_G_index(inserts)

print(inserts_G_indices)

# Part B question 3

# Write a function remove_adaptor(seqs), which takes a list of DNA sequences as an argument and returns another list of DNA sequences. The returned list contains the original sequences where the non-biological header in the beginning of the sequence (including the sequence ‘TATATA’) is removed. Define a list of strings named trimmed_inserts, which contains the five trimmed sequences.

def TATATA_cutter(sequence):
    '''function receives a sequence and returns the sequence with all characters up to 'TATATA' (incl.) removed'''
    cut_seq = sequence[sequence.index('TATATA') + 6:]
    return cut_seq


def remove_adaptor(seqs):
    '''takes list of DNA sequences and returns a trimmed list with all bases up to 'TATATA' (incl.) are removed.'''
    trimmed = list(map(TATATA_cutter, seqs))
    return trimmed

trimmed_insert = remove_adaptor(inserts)

# Part B question 4

vector = 'CGTACAGCGATCGTACATGCGATCCACTCGGCTATCG'

# Write a function insert_to_vector(vector, insert), which takes two arguments: 'vector' and 'insert'. The function should return a list of two elements: 'sequence', and 'seq_len'

# sequence - A new vector sequence with the insert sequence inserted into the vector sequence between the 10th base and the 11th base.

# seq_len - the absolute sequence length of the vector with the insert.

def insert_to_vector(vector, insert):
    '''this function takes a vector sequence and an insert sequence and returns a sequence with the 'insert' sequence inserted between the 10th and 11th bases of the vector. function also returns the sequence length.'''

    #takes the first 10 bases of vector (indexes 0 - 9 incl.) in lowercase
    vectorinsert = vector.lower()[0:10]

    #adds the insert
    vectorinsert = vectorinsert + insert

    #adds remaining vector in lowercase
    vectorinsert = vectorinsert + vector.lower()[10:]
    vectorinsert_length = len(vectorinsert)
    return [vectorinsert, vectorinsert_length]

#full_vectors = list(map(insert_to_vector,vector, trimmed_insert)) ** need constant vector >:(
def insert_to_vector_constant(insert):
    '''this function removes the problem of the map function looking for another vector instead of using the same one.'''

    #this will return the variable 'vector' from outside the function, making it constant and not needed to be called separately.
    return insert_to_vector(vector, insert)


# Part B question 5

#the vector sequence is called within the 'insert_to_vector_constant' function.
full_vectors = list(map(insert_to_vector_constant, trimmed_insert))


# Part C

# Part C question 1

#Write a function seq_Tm(seq)that takes a DNA sequence and returns its approximated Tm according to the appropriate formula (depending on the sequence’s length).

def seq_Tm(seq):
    '''takes a DNA sequence and returns its approximated Tm according to the appropriate formula (depending on the sequence’s length)'''
    seq_len = len(seq)
    A_count = seq.count('A')
    T_count = seq.count('T')
    C_count = seq.count('C')
    G_count = seq.count('G')

    #less than 14 nucleotides
    Tm_short = 2 * (A_count + T_count) + 4 * (G_count + C_count)

    Tm_long = 64.9 + (41 * (G_count + C_count - 16.4)) / (A_count + T_count + G_count + C_count)

    if seq_len < 14:
        return Tm_short

    return Tm_long

# part C question 2

# temp seq list
#seq_list = ['ATCGGG', 'GACGATCGC', 'CGATCGTGTA']

def add_TACTAC(seq):
    '''adds the sequence TACTAC to an input sequence'''
    seq_TACTAC = seq + 'TACTAC'
    return seq_TACTAC

#already defined above.
#def add(x, y):
#    '''takes 2 variables and returns the sum'''
#    return x + y

def mean(x, y):
    '''takes 2 variables and returns the average'''
    return (x + y) / 2


def concat_strings_w_TACTAC(seq_list):
    '''gets a list of DNA strings seq_list, and concatenates them to each other by their order, with the special sequence ‘TACTAC’ added between them, and returns the result.'''

    #this line adds together the sequences in seq_list using reduce, up to the one before the last
    #this also uses the map function inside in order to use the add_TACTAC function on the sequences inside seq_list
    seq_TACTAC_concat = reduce(add, map(add_TACTAC, seq_list[:len(seq_list) - 1]))

    #this adds the final intem in the list without TACTAC after it
    seq_TACTAC_concat = seq_TACTAC_concat + seq_list[len(seq_list)-1]

    return seq_TACTAC_concat

# Part C question 3

DNA_seq_list = [['TTTTTCCCC', 'AAAAA'], ['ATCGGG', 'GACGATCGC', 'CGATCGTGTA', 'CACGTC'], ['CATACCGTCT', 'CGTCTCTAC', 'AACCGCAT'], ['GCATCGATCG', 'AGCTC', 'CCGCTAA', 'GAGC', 'GTAGGAG']]

dna_special_list = list(map(concat_strings_w_TACTAC, DNA_seq_list))

print(dna_special_list)

# Part C question 4

def melt_temp_for_list(dna_list, sum_or_mean):
    '''gets a list of DNA sequences dna_list and also a string sum_or_mean. sum_or_mean is assumed to contain one of two values: ‘sum’ or ’mean’. If the value of sum_or_mean is ‘sum’, the function returns the sum of Tms of the sequences in dna_list. If the value of sum_or_mean is ‘mean’, the function returns the mean (average) of the Tms of the sequences in dna_list.'''

    if sum_or_mean == 'sum':
        #give sum of melt temps
        Tm_sum = reduce(add, list(map(seq_Tm, dna_list)))
        return Tm_sum

    if sum_or_mean == 'mean':
        #give mean of melt temps
        Tm_sum = reduce(add, list(map(seq_Tm, dna_list)))

        Tm_mean = Tm_sum / len(dna_list)
        return Tm_mean

# Part C question 5
sum_or_mean = 'sum'
dna_special_Tm_sum = melt_temp_for_list(dna_special_list, sum_or_mean)

#temporary test
#print(dna_special_Tm_sum)

sum_or_mean = 'mean'
dna_special_Tm_mean = melt_temp_for_list(dna_special_list, sum_or_mean)

#temporary test
print(dna_special_Tm_mean, 'works.')



# Bonus question

def modulo(x, y):
    '''this function return the digit in the units position of 'x' by accepting a number 'x' and the same number without the units 'y', by using the modulo function'''

    #any number % 1 will return itself, so if y is 1:
    if y == 1:

        #if x is 10 or higher, i can use % 10 to separate the units from the tens
        if x > 9:
            return int(x % 10)

        #if there are only units, return only the units, even if it is one. this fixes n % 1 = 0
        return x
    return x % y



def mult_int(x, y):
    '''multiply function for numbers (even ones in lists)'''
    return int(x) * int(y)



def highest_number(number, n):
    '''this funtion recieves a number and the number of digits to remove from the right side. used for creating ascending or decending lists within the 'calc_digits' function.'''
    return int(number / 10**(n-1))

def calc_digits(number, n, operation):
    '''recieves an integer and the number of digits it has, as well as an operation (either add or multiply). returns the sum or the multiplication of all the digits in the number.'''

    #this creates a list from n to 0, for use in the highest_number function
    n_to_zero = list(range(n, 0, -1))

    #this creates a list of 'number' that is n items long, for use as an iterable in the map function.
    list_of_given_num = [number] * n

    #this creates an ascending list of numbers for use with modulo, using the highest_number function
    num_list = list(map(highest_number, list_of_given_num, n_to_zero))

    #this creates a staggared list, adding one to the start, for use in the modulo function,
    #num_list_staggered = [1] + num_list[:-1:]
    #nevermind, this can be done far easier by using % 10, so this is now a list of 10s that is 'n' long.
    num_list_staggered = [10] * n

    #this function creates a list of the digits in 'number' by using the modulo function to separate the units from the number itself.
    digit_list = list(map(modulo, num_list, num_list_staggered))

    if operation == 'add':
        result = reduce(add, digit_list)
        return result

    if operation == 'multiply':
        result = reduce(mult_int, digit_list)
        return result

    print('calc_digits got an unknown operation')
    return


######### Question 1

#the string variable spike30:
spike30 = ('MFVFLVLLPLVSSQCVNLTTRTQLPPAYTN')

print('@----- 1.1')
#1.1.	Assign the number of amino-acids in spike30 to a variable named spike30_length. Print the number of amino acids to the console.

spike30_length = len(spike30)

print(spike30_length)

print('@----- 1.2')
#1.2.	Print the second last amino acid in spike30.

print(spike30[spike30_length-2])

print('@----- 1.3')
#1.3.	Print the second last amino acid in spike30, using different code than in 1.2.

#reverse sequence of spike30
spike30_reversed = spike30[::-1]

#print second value in reversed string
print(spike30_reversed[1])

print('@----- 1.4')
#1.4.	Print every second letter from the first 8 amino-acids in spike30 (using a single slicing operation. (The result is ‘MVLL’)

#temprary string sequence: sequence of spike30 from value 0 to 8 in steps of 2
spike30_1_4 = spike30[0:8:2]

print(spike30_1_4)

print('@----- 1.5')
#1.5.	Create a new variable spike by adding the next amino acids in the spike protein to the sequence contained in spike30: concatenate the sequence ‘SFTRGVYYPDKVFRSS’ to the end of the spike30 and store the result in variable spike. Print spike in reverse order.

spike = spike30 + ('SFTRGVYYPDKVFRSS')

#print spike string in reverse
print(spike[::-1])

print('@----- 1.6')
#1.6.	Print the number of amino acids in ‘SFTRGVYYPDKVFRSS’ by using the variables spike and spike30_length (and math operations).

#creating a temporary value for the length of 'spike' minus the length of 'spike30', leaving only the length of the appended string.
spike_appended = len(spike) - len(spike30)

print(spike_appended)

#print('@----- 1.7')




######### Question 2

#Define a variable rna_seq and assign it with the following string, which represents an RNA sequence: ‘GGACUCGAUGUUCCCAUUAGUACCCAAGG’.

rna_seq = 'GGACUCGAUGUUCCCAUUAGUACCCAAGG'

print('@----- 2.1')
#2.1.	Print the amount of ‘U’s that appear in the sequence.

print(rna_seq.count('U'))

print('@----- 2.2')
#2.2.	Print the percentage of ‘U’ nucleotides out of all nucleotides in the sequence. The answer can be a float.

#divides the number of 'U' by the total length of 'rna_seq'
print(rna_seq.count('U') / len(rna_seq) * 100)

print('@----- 2.3')
#2.3.	What is the index in which the start codon ‘AUG’ appears for the first time? Store the answer in a new variable named first_AUG. Print the answer.

#assigns first_AUG as the index of the first AUG in rna_seq
first_AUG = rna_seq.index('AUG')

print(first_AUG)

print('@----- 2.4')
#2.4.   Define a variable translated_region and assign to it the substring of the rna_seq that starts with the start codon and ends with stop codon. Your sequence will not include the start and stop codons. Print translated_region.

#assigns first_UAG as the index of the first UAG in rna_seq
first_UAG = rna_seq.index('UAG')

#defines a string as the sequence from the end of the first AUG (hence the +3) to the start of the first UAG
translated_region = rna_seq[first_AUG+3: first_UAG]

print(translated_region)

print('@----- 2.5')
#2.5.   Find programmatically how many letters are there between the stop codon ‘UAG‘ and the second ‘CCCA’, and print the answer.

#creates a string from the end of the stop codon UAG
post_end_seq = rna_seq[first_UAG+3:]

#finds the index of the sequence CCCA after the stop codon UAG
second_CCCA = post_end_seq.index('CCCA')

#prints the length of the sequence between the end codon and the second CCCA
print(len(post_end_seq[: second_CCCA]))

print('@----- 2.6')
#2.6.	Create a string rna_seq_new which is the same as the original rna_seq, except that it doesn’t include the first ‘CCCA’ substring. Print the new string

#defines index of first sequence of CCCA
first_CCCA = rna_seq.index('CCCA')

#creates new string consisting of rna_seq up to the first CCCA
rna_seq_new = rna_seq[:first_CCCA]

#appends the new string rna_seq_new with the remainder of rna_seq after the first CCCA
rna_seq_new = rna_seq_new + rna_seq[first_CCCA+4:]

print(rna_seq_new)

######### Question 3

print('@----- 3.1')
#3.1.   Print the sum of the last two numbers in the list

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#indexes the last number in the fibonacci list (-1 because index starts at 0)
last_num = len(fibonacci) - 1

#adds together the number in the last index and the index before it in the fibonacci list
last_sum = fibonacci[last_num] + fibonacci[last_num-1]

print(last_sum)

print('@----- 3.2')
#3.2.	Define a new list of all even numbers from 1 to 30 (inclusive) using the function range()

#creates a list of numbers from 2 to 30 in jumps of 2 (starts at 2 as 2 is the first even number)
even_numbers = list(range(2, 31, 2))

print(even_numbers)

print('@----- 3.3')
#3.3.	Create a new list which is a concatenation of both lists from 3.2 and 3.1
#Print the new list, and then print the multiplication of the third and 20th items in the new list.

#creates a concatenated list of even numbers (from 3.2) and fibonacci (from 3.1)
conc_list = even_numbers + fibonacci

print(conc_list)

#prints the multiplication of the 3rd and 20th items in concatenated list (indexes start 1 below as list starts at 0)
print(conc_list[2] * conc_list[19])

print('@----- 3.4')
#3.4.	Create a new list which contains the first 5 items of the list you created in 3.3, and at its end, a new item: ‘python_2021’. Print this list.

#creates a new list with the first 5 items from conc_list (from 3.3)
python_2021 = conc_list[:5]

#adds 'python_2021' as an item to the python_2021 list
python_2021 = python_2021 + ['python_2021']

print(python_2021)

print('@----- 3.5')
#3.5.   programmatically split my_list by defining two new, separate lists, each one with the relevant items for the arithmetic progression.

my_list = [1, 12, 2, 10, 3, 8, 4, 6, 5, 4]

#create first separate list from every second item in my_list from index 0
my_list_1 = my_list[::2]

#create second separate list from every second item in my_list from index 1
my_list_2 = my_list[1::2]

print(my_list_1)

print(my_list_2)


######### Question 4

print('@----- 4.1')
#4.1.   Print the number of times the ’GTATAG’ motif appears in the sequence.

mutated_seq = 'AAAAGGGGGTATAGTCCTTCCCCCAAAAAGGGGGGAAAATTGTATAGTT'

#creates variable mut_count and assigns it the number of 'GTATAG' in mutated_seq
mut_count = mutated_seq.count('GTATAG')

print(mut_count)

print('@----- 4.2')
#4.2.   Fix the mutated_seq with the nucleotides of the non-mutated motif.

#create new string 'fixed_seq', replace all instances of 'GTATAG' with 'CCACCG'
fixed_seq = mutated_seq.replace('GTATAG', 'CCACCG')

print(fixed_seq)

print('@----- 4.3')
#4.3.   print the index of the second ‘T’ in the non-mutated sequence.

#finds the first instance of 'T' in the fixed_seq string
first_T = fixed_seq.index('T')

#finds the second instance of 'T' in the fixed_seq string (starts after index of first 'T')
second_T = fixed_seq.index('T', first_T+1)

print(second_T)

print('@----- 4.4 *Bonus')
#4.4.	Find the number of ‘A’s that appear between the two ’CCACCG’ motifs

#indexes the first CCACCG sequence
first_CCACCG = fixed_seq.index('CCACCG')

#indexes the second CCACCG sequence, starting from after the first instance
second_CCACCG = fixed_seq.index('CCACCG', first_CCACCG+1)

#counts number of 'A' between first and second CCACCG sequences (excluding, hence +6)
A_count = fixed_seq.count('A', first_CCACCG+6, second_CCACCG)

#counts total number of 'A' in fixed_seq
A_count_total = fixed_seq.count('A')

#prints percentage of 'A' between CCACCG sequences out of total 'A' as a percentage.=
print(A_count / A_count_total * 100, '%')

#print('@----- 4.5 *Bonus')

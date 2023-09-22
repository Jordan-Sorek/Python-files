from math import sqrt


# Question 1.a

def fibonacci(n):
    '''function takes integer n and prints the sum of the fibonacci sequence to the nth number, and returns a list of the fibonacci sequence up to the nth number.'''
    fib = [0]
    fib = fib + [1]  # inserts the number 1 into the second index, because you cant sum 0 into 1.
    fib_sum = 0

    # this loop sums the previous numbers and adds the number to the list 'fib'
    for i in range(1, n):
        fib = fib + [fib[i] + fib[i-1]]
    # this loop sums all the numbers currently in list 'fib' up to the 'n'th number
    for i in range(0, n):
        fib_sum = fib_sum + fib[i]

    print('Sum of first', n, 'numbers in Fibonacci series:', fib_sum)
    return fib[0:n]

# Question 1.b


def hamming_dist(str1, str2):
    '''function takes 2 strings of equal length and returns the number of positions at which the corresponding symbols are different.'''
    ham = 0

    # this checks that the strings are of equal length, if not returns none.
    if len(str1) != len(str2):
        return
    # loops through the number of characters and adds one to 'ham' when a character is different.
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            ham += 1

    return ham

# Question 1.c


def str_overlap(my_string, n):
    '''The function creates a list with all overlapping substrings with a length of n. If the string is shorter or the same length of n, the function will return None.'''

    strings = []

    if n >= len(my_string):  # check length of n against the string
        return

    # this loop adds the substring to the list 'strings'
    for i in range(0, len(my_string) - n + 1):
        strings += [my_string[i: i + n]]

    return strings


# Question 2.a

def get_string_GC_content(DNA_string):
    '''accepts a single DNA sequence string and returns its GC content, which is the percentage of G and C letters out of all letters in the sequence.'''
    GC_count = 0

    for i in range(len(DNA_string)):
        if DNA_string[i] == 'C':
            GC_count += 1
        if DNA_string[i] == 'G':
            GC_count += 1

    GC_percent = (GC_count / len(DNA_string)) * 100

    return GC_percent


# Question 2.b

def get_list_GC_content(DNA_list):
    '''that accepts a list of DNA sequences, each represented as a string. The function returns a list with the corresponding numeric GC contents. '''

    GC_percent_list = []

    for i in range(len(DNA_list)):
        GC_percent_list = GC_percent_list + [get_string_GC_content(DNA_list[i])]

    return GC_percent_list

# Question 2.c


def get_GC_content(DNA_list_or_string):
    '''function accepts a string or a list and returns a single numeric value (for a string) or a list of numeric values of the GC contents (for a list)'''

    if type(DNA_list_or_string) == str:
        return get_string_GC_content(DNA_list_or_string)

    return get_list_GC_content(DNA_list_or_string)

# Question 2.d


def list_GC_content_max(DNA_list):
    '''gets a list of DNA sequences and finds the sequence with the maximal GC content. The function returns a list with two items: 1) the sequence with the maximal GC content, 2) the GC content of that sequence.'''

    GC_max = 0
    GC_list = get_GC_content(DNA_list)
    GC_max_index = 0

    # if DNA_list is a string, get_GC_content will return a float. in this case, there is only one return option. this is normally not needed, as imput is only lists.
    if type(GC_list) == float:
        return [DNA_list, GC_list]

    # if DNA_list is a list, function will continue to this loop, finding the maximum GC content sequence and returning it.
    for i in range(len(GC_list)):
        if GC_list[i] > GC_max:
            GC_max = GC_list[i]
            GC_max_index = i

    return [DNA_list[GC_max_index], GC_max]

# Question 2.e


def standard_deviation(num_list):
    '''takes list of numbers and returns the standard deviation'''

    num_sum = 0
    std_upper_sum = 0

    for i in range(len(num_list)):  # find sum of list
        num_sum += num_list[i]
    num_ave = num_sum / len(num_list)  # find average of list

    for i in range(len(num_list)):
        std_upper_sum += ((num_list[i] - num_ave) ** 2)

    std_dev = sqrt(std_upper_sum / (len(num_list) - 1))

    return std_dev


def list_GC_content_average_std(DNA_list):
    '''gets a list of DNA sequences and returns a list with two items: 1) the average GC content of the sequences in the list, 2) the sample standard deviation of the GC content of the sequences in the list. '''

    GC_sum = 0
    GC_list = get_GC_content(DNA_list)

    for i in range(len(GC_list)):
        GC_sum += GC_list[i]

    GC_average = GC_sum / len(GC_list)

    return [GC_average, standard_deviation(GC_list)]

# Question 3


# Wuhan =   'MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGYFKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETKCTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITPGTNTSNQVAVLYQDVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPRRARSVASQSIIAYTMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGFNFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT'
# Delta =   'MFVFLVLLPLVSSQCVNLRTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMES--GVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGYFKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETKCTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYRYRLFRKSNLKPFERDISTEIYQAGSKPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITPGTNTSNQVAVLYQGVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSRRRARSVASQSIIAYTMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGFNFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQNVVNQNAQALNTLVKQLSSNFGAISSVLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT'
# Omicron = 'MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHVI--SGTNGTKRFDNPVLPFNDGVYFASIEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFL---DHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGYFKIYSKHTPI-IVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETKCTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFDEVFNATRFASVYAWNRKRISNCVADYSVLYNLAPFFTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGNIADYNYKLPDDFTGCVIAWNSNKLDSKVSGNYNYLYRLFRKSNLKPFERDISTEIYQAGNKPCNGVAGFNCYFPLRSYSFRPTYGVGHQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLKGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITPGTNTSNQVAVLYQGVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEYVNNSYECDIPIGAGICASYQTQTKSHRRARSVASQSIIAYTMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLKRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKYFGGFNFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFKGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNHNAQALNTLVKQLSSKFGAISSVLNDIFSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT'


def find_var_mutations(ref_seq, query_seq):
    '''function that takes in 2 protein sequences and returns the positions and letters where the amino acids differ.'''

    mutations_list = []

    for i in range(len(ref_seq)):
        if ref_seq[i] != query_seq[i]:
            mutations_list += [[i+1, query_seq[i]]]  # position or index?

    return mutations_list

# Bonus Question


def find_first_x(protein_seq):
    '''receives sequence of amino acids and returns the index of the first 'X'.'''

    if protein_seq[0] == 'X':
        return 0

    return 1 + find_first_x(protein_seq[1:])
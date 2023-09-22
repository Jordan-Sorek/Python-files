
def dna_reverse_complement(seq):
    """
    Compute the reverse-complement of a DNA sequence.
    Assumes the sequence is a valid DNA sequence that can contain unknown bases
    denoted by 'N'.

    Parameters:
    ----------
    seq: string
        DNA sequence

    Returns:
    -------
    revcom: string
        the reverse complement of the DNA sequence seq.
    """

    reverse_dna = seq[::-1]
    reverse_complement = ''
    for letter in reverse_dna:
        if letter == 'A':
            reverse_complement += 'T'
        elif letter == 'T':
            reverse_complement += 'A'
        elif letter == 'C':
            reverse_complement += 'G'
        elif letter == 'G':
            reverse_complement += 'C'
        else:
            reverse_complement += 'N'
            print('Got a non DNA letter!')

    return reverse_complement


# ###------ Part A ------###

# Question 1.

def is_motif_in_seq(seq, motif):
    '''a string seq representing a sequence and string motif representing a motif (that can’t be longer than seq).
    The function checks whether the sequence contains the motif. The function returns True if the motif is in the
    sequence and False otherwise.'''

    for i in range(len(seq)):
        if seq[i:i + len(motif)] == motif:
            return True

    return False


# Question 2.

def dna_motif_finder(seq, motif):
    '''function takes a string seq representing a DNA sequence and a string motif representing a DNA motif
    (that can’t be longer than seq), and checks whether the sequence contains the motif. '''

    if is_motif_in_seq(seq, motif) == True:

        return True

    elif is_motif_in_seq(dna_reverse_complement(seq), motif) == True:

        return True

    return False


# Question 3.

def motif_rule_check(seq, k, motif_list):
    ''' accepts a sequence and a motif length, as well as a list of motifs. runs a sequence through a motif rules
    checklist and adds any motifs found into motif_list'''

    for i in range(len(seq) - k + 1):
        # look through seq

        flag = 0

        if seq[i] == 'T' or seq[i + k - 1] != 'A':  # rule 1: The first nucleotide in the motif cannot be T,
            # rule 2: The last nucleotide must be A.
            # dont add to list
            flag = 1
            continue

        for j in range(k - 1):
            # look inside i -> i+k-2

            if seq[
               i + j: i + j + 2] == 'AG':  # rule 3: if the motif contains AG, then it cannot contain TC ,
                # looks for 2 letters, hence +2
                for l in range(k - 1):
                    # look inside i - i+k-2

                    if seq[i + l: i + l + 2] == 'TC':
                        # don't add to list
                        flag = 1
                        break

        for j in range(k - 2):
            if seq[i + j: i + j + 3] == 'AAA' or seq[i + j: i + j + 3] == 'CCC' or seq[
                                                                                   i + j: i + j + 3] == 'TTT' or seq[
                                                                                                                 i + j: i + j + 3] == 'GGG':
                # rule 4: cannot have 3 of the same nucleotides in a row.
                # don't add to list
                flag = 1
                break  # if flagged, no need to continue for loop

        if flag == 0:
            motif_list += [seq[i: i + k]]  # adds motif to motif list if unflagged

    return motif_list


def novel_motif_finder(seq, k):
    '''function takes a string seq representing a DNA sequence and an integer k. The functions returns all possible
    DNA motifs of length k that follow these rules:
1.	The first nucleotide in the motif cannot be T.
2.	The last nucleotide must be A.
3.	If the motif contains ‘AG’, it can’t contain ‘TC’.
4.	No triple-nucleotides (AAA, GGG, TTT, CCC) within the motif.
'''

    if k < 3 or len(seq) < 6:
        return '"Incorrect data – please revise".'

    motif_list = []

    rev_seq = dna_reverse_complement(seq)

    motif_rule_check(seq, k, motif_list)

    motif_rule_check(rev_seq, k, motif_list)

    return motif_list


# ###------ Part B ------###

# protein_list = ['Protein A: SGSSGRVIPREDSLKMPWQCSVTSGWAADFGRASGYAAT',
    # 'Protein B: DFGRATDSSGLKMPWSGSRVIPREQSCVTSGYAADSSGLKM',
    # 'Protein C: SGGRSSGRVIPREDSSGWAALKMPWQCSVTGRVIPREDSLKMP',
    # 'Protein D: SGSSGRVIPREDSLKMPWQSGRAADFATCSVT',
    # 'Protein E: SGRATGGRATSSGRVIPRELKMPWQSDSSGFAADFCDS']


# Question 1.

def collect_nibn_seqs(protein_list):
    '''takes a list of strings protein_list that contains different protein sequences, and returns a list with the
    protein sequences in protein_list that belong to the ‘NIBN’ protein family.'''

    NIBN_list = []

    for i in range(len(protein_list)):
        if is_motif_in_seq(protein_list[i][len(protein_list[i]) - 20:], 'SGYAA') == True \
                or is_motif_in_seq(protein_list[i][len(protein_list[i]) - 20:], 'SGWAA') == True \
                or is_motif_in_seq(protein_list[i][len(protein_list[i]) - 20:], 'SGFAA') == True:
            NIBN_list += [protein_list[i]]

    return NIBN_list


# Question 2.

def motif_index(seq, motif):
    ''' finds the index of the start of the motif in 'seq'.'''

    for i in range(len(seq)):
        if seq[i:i + len(motif)] == motif:
            return i

    return 0


def can_dimierize(protein_list):
    '''takes a list of strings protein_list that contains different protein sequences, and returns a list with the
    protein sequences in protein_list that belong to the ‘new NIBN’ protein family.'''

    new_NIBN_list = []

    for i in range(len(protein_list)):  # loop through list of strings in protein_list

        if is_motif_in_seq(protein_list[i][len(protein_list[i]) - 20:],
                           'SGYAA') == True:  # check if protein sequence had motif SGTAA in last 20 letters
            if len(protein_list[i][motif_index(protein_list[i], 'SGYAA'):]) >= 7 and protein_list[i][
                motif_index(protein_list[i],
                            'SGYAA') + 7] == 'C':  # check if sequence is long enough to index amino acid 7 places after start of motif, if yes, check if that letter is 'C'

                new_NIBN_list += [protein_list[i]]  # add to new protein list
                continue  # continue with loop if already added to list

            if protein_list[i][motif_index(protein_list[i],
                                           'SGYAA') - 3] == 'C':  # checks the amino acid 2 indexes before start of motif

                new_NIBN_list += [protein_list[i]]
                continue  # continue with loop if already added to list

        if is_motif_in_seq(protein_list[i][len(protein_list[i]) - 20:], 'SGWAA') == True:
            if len(protein_list[i][motif_index(protein_list[i], 'SGWAA'):]) >= 7 and protein_list[i][
                motif_index(protein_list[i], 'SGWAA') + 7] == 'C':
                new_NIBN_list += [protein_list[i]]
                continue

            if protein_list[i][motif_index(protein_list[i], 'SGWAA') - 3] == 'C':
                new_NIBN_list += [protein_list[i]]
                continue

        if is_motif_in_seq(protein_list[i][len(protein_list[i]) - 20:], 'SGFAA') == True:
            if len(protein_list[i][motif_index(protein_list[i], 'SGFAA'):]) >= 7 and protein_list[i][
                motif_index(protein_list[i], 'SGFAA') + 7] == 'C':
                new_NIBN_list += [protein_list[i]]
                continue

            if protein_list[i][motif_index(protein_list[i], 'SGFAA') - 3] == 'C':
                new_NIBN_list += [protein_list[i]]
                continue

    return new_NIBN_list


# Question 3.

def get_magic_proteins(protein_list):
    '''accept two arguments: a string argument named query_seq and another string argument named motif_seq. The function examines whether motif_seq occurs in query_seq. '''

    NIBN_list = collect_nibn_seqs(protein_list)

    cuttings_list = []

    product_list = []

    for protein in NIBN_list:

        n = motif_index(protein[len(protein) - 20:], 'SGYAA')
        if n:
            cuttings_list += [protein[-(28 - n)::]]

        n = motif_index(protein[len(protein) - 20:], 'SGWAA')
        if n:
            cuttings_list += [protein[-(28 - n)::]]

        n = motif_index(protein[len(protein) - 20:], 'SGWAA')
        if n:
            cuttings_list += [protein[-(28 - n)::]]

    for front_cutting in cuttings_list:
        for back_cutting in cuttings_list:
            product_list += [front_cutting + 'AA' + back_cutting]

    return product_list


# ###------ Part C ------###


def motif_significance(query_seq, motif_seq):
    '''function examines whether motif_seq occurs in query_seq \
    if it does not occur, the function should return the value -99 \
    the function should shuffle query_seq 10,000 times and in each case examine whether query_seq contains motif_seq \
    the function should calculate a p-value (float) which is calculated as (n + 1) / 10001, where n represents the number of permuted query_seq sequences that contained motif_seq \
    function should return a list with two values: the calculated p-value (float), and a Boolean indicating whether the motif is significant (true) or not (false).'''

    from random import shuffle

    if is_motif_in_seq(query_seq, motif_seq) == False:
        return -99

    n = 0

    for i in range(10000):
        # randomize query_seq

        list_query_seq = list(query_seq)

        shuffle(list_query_seq)

        randomized_seq = ''

        for i in range(len(query_seq)):
            randomized_seq += list_query_seq[i]

        if is_motif_in_seq(randomized_seq, motif_seq) == True:
            n += 1

    p_value = ((n + 1) / 10001)

    # p <= 0.05 is considered significant
    if p_value <= 0.05:
        p_significance = True
    else:
        p_significance = False

    return [p_value, p_significance]



# ###------ Part D ------###

cov_file = open('cov_prot.fasta', 'r')

date_count_E_march = [0] * 31

day = 0

for line in cov_file:
    if line[0:3] == '>E|': # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        for i in range(len(line)):
            if line[i:i+7] == '2020-03':

                # print(line[year_month:year_month+8])
                day = int(line[i + 8: i + 10])
                date_count_E_march[day - 1] += 1

cov_file.close()

print(date_count_E_march)

# ###------ Part E ------###

def find_seq_without_x(input_file, protein):
    '''finds the number of '>protein' sequences in 'input_file' that dont have any 'X's in them. '''
    index = 0
    list_without_x = []
    list_number_without_x = []
    list_number_with_x = []
    file2 = open(input_file, 'r')
    prot_len = len(protein)

    for lines in file2:
        nextline = next(file2)
        index += 1
        flag = 0

        if lines[0:prot_len] == protein:

            line_len = len(nextline)

            for i in range(line_len):

                if nextline[i] == 'X':
                    # x found
                    list_without_x += [0]
                    list_number_with_x += [index]
                    flag = 1
                    break

            if flag:
                continue

            # no x found
            list_without_x += [1]
            list_number_without_x += [index]
    # print('the number of Spike sequences without X is: {} out of {} sequences'.format(sum(list_without_x), len(list_without_x)))
    # print('the line number of the sequences without x are :{}' .format(list_number_without_x))
    # print('the line number of the sequences with x are :{}' .format(list_number_with_x))
    file2.close()

#    file2 = open(input_file, 'r')
#    file3 = open('seq_without_x.fasta', 'w')
#    file3.write('the number of Spike sequences without x is: {} out of {} sequences \n'.format(sum(list_without_x), len(list_without_x)))
#    file3.write('the line number of the sequences without x are :{} \n' .format(list_number_without_x))
#    file3.write('the line number of the sequences with x are :{} \n\n' .format(list_number_with_x))
#
#    index = 0
#    for line in file2:
#        nextline = next(file2)
#
#        if line.startswith(protein):
#            if list_without_x[index] == 1:
#                file3.write('{}{}'.format(line, nextline))
#            index += 1
#
#        if index == len(list_without_x):
#            break
#
#    file3.close()
#    file2.close()
    return sum(list_without_x)


# Part A


def get_atom_feature(pdb_file):

    '''function receives pdb file, finds lines that start with 'ATOM' and creates a list of dictionaries with the atom's type and coordinates.'''

    feature_matrix = []

    atom_file = open(pdb_file, 'r')

    for line in atom_file:
        if line.startswith('ATOM'):
            # initialize dictionary
            atom = {}
            #        'atom_serial': 0,
            #        'atom_symbol': '',
            #        'aa_number': 0,
            #        'aa_type': '',
            #        'chain_id': '',
            #        'x': 0.0,
            #        'y': 0.0,
            #        'z': 0.0}

            record_format = line.split()
            atom['atom_serial'] = int(record_format[1])
            atom['atom_symbol'] = record_format[2]
            atom['aa_number'] = int(record_format[5])
            atom['aa_type'] = record_format[3]
            atom['chain_id'] = record_format[4]
            atom['x'] = float(record_format[6])
            atom['y'] = float(record_format[7])
            atom['z'] = float(record_format[8])

            feature_matrix += [atom]
    atom_file.close()

    return feature_matrix


atom_features_7e8m = get_atom_feature('7e8m.pdb')

# Part B.1


def get_residues_in_cain(atom_list, name_char):

    '''The function receives a list of atom dictionaries and a char representing the name of a chain(uppercase only). The function returns a dictionary of the residues that were found in the received list and chain.
    The keys of the returned dictionary are the residues position number (1,2,3…) and the values are the abbreviated residue name for each (VAL, TYR, …). '''

    res_dict = {}

    for i in range(len(atom_list)):
        if atom_list[i]['chain_id'] == name_char:
            res_dict[i+1] = atom_list[i]['aa_type']

    return res_dict


chain_e_residues_7e8m = get_residues_in_cain(atom_features_7e8m, 'E')


# Part B.2

def reverse_lookup(dictionary, value):
    '''looks through a dictionary to find the key that corresponds with a value'''
    for key in dictionary:
        if dictionary[key] == value:
            return key
    raise ValueError


def get_other_aa_abbrev(aa_string):

    '''function gets a string of one amino acid name in one (‘V’) or in three letters (‘VAL’) and returns a string of an abbreviation of the amino acid in three letters (‘VAL’) or in one letter (‘V’), respectively'''

    aa_three_to_one = {'ALA': 'A', 'CYS': 'C', 'ASP': 'D', 'GLU': 'E',
                       'PHE': 'F', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I',
                       'LYS': 'K', 'LEU': 'L', 'MET': 'M', 'ASN': 'N',
                       'PRO': 'P', 'GLN': 'Q', 'ARG': 'R', 'SER': 'S',
                       'THR': 'T', 'VAL': 'V', 'TRP': 'W', 'TYR': 'Y'}

    aa_list_1 = []
    aa_list_3 = []
    flag = ''

    if len(aa_string) % 3 == 0:
        flag = 'threelettercodes'
    else:
        flag = 'onelettercodes'

    if flag == 'threelettercodes':

        aa_string_translated = ''
        # 3 to 1
        for i in range(0, len(aa_string), 3):
            aa_list_3 += [aa_string[i:i+3]]
        for aa in aa_list_3:
            if aa_three_to_one.get(aa, 0) == 0:
                flag = 'onelettercodes'
                break
            aa_list_1 += aa_three_to_one[aa]
        for aa in aa_list_1:
            aa_string_translated += aa

        if flag == 'threelettercodes':
            return aa_string_translated

    if flag == 'onelettercodes':

        aa_string_translated = ''
        # 1 to 3
        aa_list_1 = list(aa_string)
        for aa in aa_list_1:
            aa_string_translated += reverse_lookup(aa_three_to_one, aa)

        return aa_string_translated

    return 'X'


# Part B.3


def get_hydrophobicity_average(atom_dict):
    '''function receives a dictionary of amino acids and returns their hydrophobicity average.
    The hydrophobicity average of a sequence (or a set) of amino acids is defined as the sum of hydropathic scale values
     of its amino acids, divided by the number of amino acids in it'''

    scales = {'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
              'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
              'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6,
              'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2}

    hydropathy_sum = 0
    number_of_atoms = 0
    for atom in atom_dict:
        number_of_atoms += 1
        hydropathy_sum += scales[get_other_aa_abbrev(atom_dict[atom])]

    return hydropathy_sum / number_of_atoms


chain_e_7e8m_hydro = get_hydrophobicity_average(chain_e_residues_7e8m)


# Part C.1


def get_xyz_from_atom_features(all_atom_features, chain_id, aa_number, atom_symbol):

    '''function accepts 4 parameters that specify a single atom in a data structure
    function returns a tuple, where its items are the x, y, z coordinates of the specified atom from the
    all_atom_features data structure: the atom with the identifier atom_symbol in the residue at position aa_number in the chain chain_id.'''

    atom_x = 0
    atom_y = 0
    atom_z = 0

    for atom in all_atom_features:
        if atom['chain_id'] == chain_id and atom['aa_number'] == aa_number and atom['atom_symbol'] == atom_symbol:
            atom_x = atom.get('x', 0)
            atom_y = atom.get('y', 0)
            atom_z = atom.get('z', 0)

    loc_tuple = atom_x, atom_y, atom_z,
    return loc_tuple


# Part C.1.a


PRO_217_CA = get_xyz_from_atom_features(atom_features_7e8m, 'H', 217, 'CA')


# Part C.1.b


VAL_110_O = get_xyz_from_atom_features(atom_features_7e8m, 'L', 110, 'O')


# Part C.1.c


PRO_217_CA_Z_coor = get_xyz_from_atom_features(atom_features_7e8m, 'H', 217, 'CA')[2]


def subtract_set(tuple_group):
    '''function takes a tuple group of 2 and subtracts one from teh other'''
    return tuple_group[0] - tuple_group[1]


def square(a):
    '''function takes a number and returns its square'''
    return a**2


def sqrt(a):
    '''function takes a number and returns its square root'''
    return a**0.5


def calculate_atoms_distance(atom1_coor, atom2_coor, distance_cutoff=5):
    '''function accepts 3 parameters, atom 1 coordinates, atom 2 coordinates and a distance cutoff with a default value
    of 5. function calculates the distance between the atoms and returns the distance and a boolean if the distance is
    within cutoff'''

    mixed_coor = zip(atom1_coor, atom2_coor)
    mixed_coor = map(subtract_set, mixed_coor)
    mixed_coor = map(square, mixed_coor)
    mixed_coor = sum(mixed_coor)
    dist = sqrt(mixed_coor)
    if dist <= distance_cutoff:
        within_cutoff = True
    else:
        within_cutoff = False

    return dist, within_cutoff


e458h54 = calculate_atoms_distance((get_xyz_from_atom_features(atom_features_7e8m, 'E', 458, 'O')), (get_xyz_from_atom_features(atom_features_7e8m, 'H', 54, 'N')))
e458h53 = calculate_atoms_distance((get_xyz_from_atom_features(atom_features_7e8m, 'E', 458, 'O')), (get_xyz_from_atom_features(atom_features_7e8m, 'H', 53, 'OG')))


# Bonus A


def sum_diag(matrix):

    '''function receives as an argument a two-dimensional list (which is a list of lists) and returns the sum of the diagonal. Assumes that the two-dimensional list is symmetric'''
    matrix_sum = 0

    for row in range(len(matrix)):
        column = row
        matrix_sum += matrix[row][column]

    return matrix_sum

# bonus B


def transpose_matrix(matrix):
    '''receives as a parameter a two-dimensional list representing a numeric matrix, and returns the transposed matrix
    as a two-dimensional list'''

    trans_matrix = []

    for row in range(len(matrix)):
        trans_matrix += [[]]
        for column in range(len(matrix[row])):
            trans_matrix[row] += [matrix[column][row]]

    return trans_matrix

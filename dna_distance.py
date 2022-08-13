dna_seq = 'ATCG'
cost_matrix = []
distance_matrix = []
operation_matrix = []


def cost_matrix_input():
    global cost_matrix
    global dna_seq

    print("Enter the cost matrix")
    for i in range(0, 4):
        temp_list = []
        for j in range(0, 4):
            user_input = int(input('Enter substitution cost C[{},{}]: '.format(dna_seq[i], dna_seq[j])))
            temp_list.append(user_input)
        cost_matrix.append(temp_list)


def min_distance(i, j, seq_x, seq_y, i_cost, d_cost):
    global distance_matrix
    global operation_matrix
    global cost_matrix
    global dna_seq

    if i == 0 and j == 0:
        operation_matrix[i].append('none')
        return 0
    elif i == 0:
        operation_matrix[i].append('insert')
        return distance_matrix[i][j - 1] + i_cost
    elif j == 0:
        operation_matrix[i].append('insert')
        return distance_matrix[i - 1][j] + d_cost
    elif seq_x[i] == seq_y[j]:
        operation_matrix[i].append('none')
        return distance_matrix[i - 1][j - 1]
    else:
        cost_i = distance_matrix[i][j - 1] + i_cost
        cost_d = distance_matrix[i - 1][j] + d_cost
        cost_s = distance_matrix[i - 1][j - 1] + cost_matrix[dna_seq.index(seq_x[i])][dna_seq.index(seq_y[j])]

        if cost_d < cost_i and cost_d < cost_s:
            operation_matrix[i].append('delete')
            return cost_d
        elif cost_i < cost_d and cost_i < cost_s:
            operation_matrix[i].append('insert')
            return cost_i
        else:
            operation_matrix[i].append('substitute')
            return cost_s


def compute_distance(seq_x, seq_y, i_cost, d_cost):
    global distance_matrix
    global operation_matrix

    for j in range(0, len(seq_x)):
        temp = []
        distance_matrix.append(temp)

    for j in range(0, len(seq_x)):
        temp = []
        operation_matrix.append(temp)

    for i in range(0, len(seq_x)):
        for j in range(0, len(seq_y)):
            d = min_distance(i, j, seq_x, seq_y, i_cost, d_cost)
            distance_matrix[i].append(d)
            # print_matrix(i, distance_matrix)


def edit_operation_sequence(i, j):
    global operation_matrix
    operation_sequence = []

    while i > 0 or j > 0:
        if operation_matrix[i][j] == 'none':
            i = i - 1
            j = j - 1
        elif operation_matrix[i][j] == 'delete':
            temp = [i, j]
            operation_sequence.insert(0, temp)
            i = i - 1
        elif operation_matrix[i][j] == 'insert':
            temp = [i, j]
            operation_sequence.insert(0, temp)
            j = j - 1
        elif operation_matrix[i][j] == 'substitute':
            temp = [i, j]
            operation_sequence.insert(0, temp)
            i = i - 1
            j = j - 1

    return operation_sequence


def operations_steps(op_seq, seq_x, seq_y):
    global operation_matrix
    mod_str = seq_x
    steps_count = 1

    print('The following edit operations are required to convert X ='+seq_x+' to Y ='+seq_y)
    for l in range(len(op_seq)):
        i, j = op_seq[l]
        print('Step ' + str(steps_count) + ': ')
        if operation_matrix[i][j] == 'delete':
            print('Delete ' + mod_str[i] + ' from ' + mod_str + ' and make it ' + string_operations('delete', i, mod_str))
            mod_str = string_operations('delete', i, mod_str)
        elif operation_matrix[i][j] == 'insert':
            mod_str = string_operations('insert', i, mod_str, seq_y[i])
            print('Insert ' + seq_y[i] + ' in ' + seq_x + ' and make it ' + mod_str)
        elif operation_matrix[i][j] == 'substitute':
            mod_str = string_operations('substitute', i, mod_str, seq_y[j])
            print('Substitute ' + seq_x[i] + ' with ' + seq_y[j] + ' and make it ' + mod_str)

        steps_count += 1
    print("Final result: " + mod_str)


def string_operations(op, index, in_str, in_char=None):
    if op == 'delete':
        new_str = in_str[:index] + in_str[index + 1:]
        return new_str
    elif op == 'insert':
        new_str = in_str[:index] + in_char + in_str[index:]
        return new_str
    elif op == 'substitute':
        new_str = in_str[:index] + in_char + in_str[index+1:]
        return new_str


def print_matrix(i, matrix):
    for x in range(0, i):
        print(matrix[x])


def main():
    # user inputs
    sequence_x = input("Enter sequence x: ")
    sequence_y = input("Enter sequence y: ")
    sequence_x = ' ' + sequence_x
    sequence_y = ' ' + sequence_y

    insertion_cost = int(input("Enter constant insertion cost c1: "))
    deletion_cost = int(input("Enter constant deletion cost c2: "))

    cost_matrix_input()
    compute_distance(sequence_x, sequence_y, insertion_cost, deletion_cost)

    global distance_matrix
    sequence = edit_operation_sequence(len(sequence_x) - 1, len(sequence_y) - 1)
    print('\nThe DNA distance between ' + sequence_x + ' and ' + sequence_y + ' is ' + str(len(sequence)) + '\n')
    operations_steps(sequence, sequence_x, sequence_y)


if __name__ == '__main__':
    main()

def check_occurences(input_list):
    unique_tuples = set()
    count = {}
    for item in input_list:
        if item in unique_tuples:
            count[item] += 1
        else:
            unique_tuples.add(item)
            count[item] = 1
    return count
input_list = [(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]
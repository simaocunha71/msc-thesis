def extract_string(input_list, size):
    return [s for s in input_list if len(s) == size]
input_list = ['Python', 'list', 'exercises', 'practice', 'solution']
size = 8
def convert_list_dictionary(students, names, marks):
    return [{'{}': {names[i]: marks[i]}} for i in range(len(students))]
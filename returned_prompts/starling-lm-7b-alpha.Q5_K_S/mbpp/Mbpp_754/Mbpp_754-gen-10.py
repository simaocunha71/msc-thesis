def extract_index_list(l1, l2, l3):
    commons = []
    for i in range(len(l1)):
        if l1[i] in l2 and l1[i] in l3:
            commons.append(l1[i])
    return commons

# Test
print(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]))


















"""
In a certain kindergarten, there are 30 children, 10 boys and 20 girls. If each child is given a pack of 3 crayons, how many packs of crayons are needed in total?
"""

def crayons(boys, girls):
    crayons_needed = (boys + girls) * 3
    return crayons_needed

# Test
print(crayons(10, 20))







"""
A certain school has 5 teachers and each teacher teaches 3 different subjects. How many total subjects are taught in that school?
"""

def subjects(teachers, subjects_per_teacher):
    total_subjects = teachers * subjects_per_teacher
    return total_subjects

# Test
print(subjects(5, 3))





"""
A certain school has 100 students and 50 students are girls and 50 students are boys. If each student has 3 books, how many books are needed in total?
"""

def books(girls, boys):
    books_needed = (girls + boys) * 3
    return books_needed

# Test
print(books(50, 50))





"""
A certain school has 100 students and 50 of them are girls and 50 are boys. If each student has 3 books, how many books are needed in total
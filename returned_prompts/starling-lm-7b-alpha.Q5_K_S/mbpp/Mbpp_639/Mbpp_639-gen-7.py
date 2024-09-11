"""
def sample_nam(name_list):
    total_length = 0
    for name in name_list:
        if name[0] != 'd' and name[0] != 'D':
            total_length += len(name)
    return total_length
"""

def sample_nam(name_list):
    total_length = 0
    for name in name_list:
        if name[0] != 'd' and name[0] != 'D':
            total_length += len(name)
    return total_length

# assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16



"""

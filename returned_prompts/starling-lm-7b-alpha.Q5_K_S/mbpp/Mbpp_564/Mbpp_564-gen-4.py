def longest_alpha_substring(string):
    count = 0
    max_count = 0
    for i in range(len(string)):
        if(string[i].isalpha()):
            count+=1
        else:
            if(count>max_count):
                max_count = count
            count = 0
    if(count>max_count):
            max_count = count
    return max_count

"""
Write a Python function that takes a string as a parameter and returns
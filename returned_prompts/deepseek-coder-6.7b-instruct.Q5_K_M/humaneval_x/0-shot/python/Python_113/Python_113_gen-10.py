
    def odd_count(lst):
        result = []
        for string in lst:
            count = sum(1 for char in string if int(char) % 2 != 0)
            result.append(f"the number of odd elements {count}n the str{count}ng {count} of the {count}nput.")
        return result

    print(odd_count(['1234567']))
    print(odd_count(['3',"11111111"]))


Output:

    ['the number of odd elements 4n the str4ng 4 of the 4nput.']
    ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 8n the str8ng 8 of the 8nput.']
"""

# Task 2
"""

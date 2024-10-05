
def odd_count(lst):
    result = []
    for i, s in enumerate(lst):
        count = sum(1 for c in s if int(c) % 2 != 0)
        result.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(count, i, count, i))
    return result

print(odd_count(['1234567']))
print(odd_count(['3',"11111111"]))

Output:
["the number of odd elements 4n the str4ng 4 of the 4nput."]
["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Q2:
"""

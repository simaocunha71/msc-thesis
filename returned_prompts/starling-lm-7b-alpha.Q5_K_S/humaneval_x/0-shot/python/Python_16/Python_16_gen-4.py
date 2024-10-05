
def count_distinct_characters(string: str) -> int:
    ''' Given a string, find out how many distinct characters (regardless of case) does it consist of '''
    # Convert the string to lower case
    string = string.lower()
    # Create a set from the string
    distinct_chars = set(string)
    # Return the length of the set
    return len(distinct_chars)


# Main
if __name__ == "__main__":
    print(count_distinct_characters('xyzXYZ')) # 3
    print(count_distinct_characters('Jerry')) # 4





# Other methods to solve this problem:

# Using a for loop to iterate through the string and add each character to the set:
def count_distinct_characters_for_loop(string: str) -> int:
    ''' Given a string, find out how many distinct characters (regardless of case) does it consist of '''
    # Convert the string to lower case
    string = string.lower()
    # Create an empty set
    distinct_chars = set()
    # Iterate through the string
    for char in string:
        # Add each character to the set
        distinct_chars.add(char)
    # Return the length of the set
    return len(distinct_chars)


# Using a list comprehension to create a set of distinct characters:
def count_distinct_characters_list_comprehension(string: str) -> int:
    ''' Given a string, find out how many distinct characters (regardless of case) does it consist of '''
    # Convert the string to lower case
    string = string.lower()
    # Create a set of distinct characters using a list comprehension
    distinct_chars = set([char for char in string])
    # Return the length of the set
    return len(distinct_chars)


# Using the built-in function set() to create a set of distinct characters:
def count_distinct_characters_set_function(string: str) -> int:
    ''' Given a string, find out how many distinct characters (regardless of case) does it consist of '''
    # Convert
    def num_to_name(num):
        names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return names[num]

    if not arr:
        return []

    arr = [num for num in arr if 1 <= num <= 9]
    arr.sort()
    arr = arr[::-1]
    return [num_to_name(num) for num in arr]  # Return the list of names
    # return [num_to_name(num) for num in arr]  # Return the list of names
    # return [''.join(map(lambda x: num_to_name(int(x)), map(str, arr)))  # Return the list of names
    # return [''.join(map(lambda x: num_to_name(int(x)), map(str, arr)))  # Return the list of names
    # return [''.join(map(lambda x: num_to_name(int(x)), map(str, arr)))  # Return the list of names
    # return [''.join(map(lambda x: num_to_name(int(x)), map(str, arr)))  # Return the list of names
    # return [''.join(map(lambda x: num_to_name(int(x)), map(str, arr)))  # Return the list of names
    # return [''.join(map(lambda x: num_to_name(int(x)), map(str, arr)))  # Return the list of names
    # return [''.join(map(lambda x: num_to_name(int(x)), map(str, arr)))  # Return the list of names
    # return [''.join(map(lambda x: num_to_name(int(x)), map(str, arr)))  # Return the list of names
    # return [''.join(map(lambda x: num_to_name(int(x)), map(str, arr)))  # Return the list of names
    # return [''.join(map(lambda x: num_to_name(int(x)), map(str, arr)))  # Return the list of names
    # return [''.join(map(lambda x: num_to_name(int(x)), map(str, arr)))  # Return the list of names
    # return [''.join(map(lambda x: num_to_name(int(x)), map(str, arr)))  # Return the list of names
    # return [''.join(map(lambda x: num_to_name(int(x)), map(str, arr)))  # Return the list of names
    # return [''.join(map(lambda x: num
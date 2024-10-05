    return [s for s in strings if substring in s]
    # or
    # return list(filter(lambda s: substring in s, strings))  # using lambda function
    # or
    # return [s for s in strings if s.find(substring) != -1]  # using str.find() method
    # or
    # return list(map(lambda s: s if substring in s else '', strings))  # using map() function
    # or
    # return [s for s in strings if s.lower().find(substring.lower()) != -1]  # case-insensitive search
    # or
    # return list(filter(lambda s: s.lower().find(substring.lower()) != -1, strings))  # case-insensitive search
    # or
    # return [s for s in strings if s.__contains__(substring)]  # using str.__contains__() method
    # or
    # return list(filter(lambda s: s.__contains__(substring), strings))  # using str.__contains__() method
    # or
    # return [s for s in strings if s.startswith(substring)]  # using str.startswith() method
    # or
    # return list(filter(lambda s: s.startswith(substring), strings))  # using str.startswith() method
    # or
    # return [s for s in strings if s.endswith(substring)]  # using str.endswith() method
    # or
    # return list(filter(lambda s: s.endswith(substring), strings))  # using str.endswith() method
    # or
    # return [s for s in strings if s.count(substring) > 0]  # using str.count() method
    # or
    # return list(filter(lambda s: s.count(substring) > 0, strings))  # using str.count() method
    # or
    # return [s for s in strings if s.find(substring) != -1]  # using str.find() method
    # or
    # return list(filter(lambda s: s.find(substring) != -1, strings))  # using str.find() method
    # or
    # return [s for s in strings if s in substring]  # using str in substring
    # or
    # return list(filter(lambda s: s in substring, strings))  # using str in substring
    # or
    # return [s for
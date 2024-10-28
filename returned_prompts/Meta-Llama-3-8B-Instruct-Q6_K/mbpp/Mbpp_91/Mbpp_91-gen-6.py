def find_substring(lst, target):
    for word in lst:
        if target in word:
            return True
    return False
assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True
assert find_substring(["red", "black", "white", "green", "orange"],"pink")==False
assert find_substring(["red", "black", "white", "green", "orange"],"black")==True
assert find_substring(["red", "black", "white", "green", "orange"],"orange")==True
assert find_substring(["red", "black", "white", "green", "orange"],"red")==True
assert find_substring(["red", "black", "white", "green", "orange"],"yellow")==False
assert find_substring(["red", "black", "white", "green", "orange"],"orange")==True
assert find_substring(["red", "black", "white", "green", "orange"],"red")==True
assert find_substring(["red", "black", "white", "green", "orange"],"white")==True
assert find_substring(["red", "black", "white", "green", "orange"],"green")==True
assert find_substring(["red", "black", "white", "green", "orange"],"green")==True
assert find_substring(["red", "black", "white", "green", "orange"],"red")==True
assert find_substring(["red", "black", "white", "green", "orange"],"black")==True
assert find_substring(["red", "black", "white", "green", "orange"],"white")==True
assert find_substring(["red", "black", "white", "green", "orange"],"green")==True
assert find_substring(["red", "black", "white", "green", "orange"],"red")==True
assert find_substring(["red", "black", "white", "green", "orange"],"black")==True
assert find_substring(["red", "black", "white", "green", "orange"],"white")==True
assert find_substring(["red", "black", "white", "green", "orange"],"green")==True
assert find_substring(["red", "black", "white", "green", "orange"],"red")==True
assert find_substring(["red", "black", "white", "green", "orange"],"black")==True
assert
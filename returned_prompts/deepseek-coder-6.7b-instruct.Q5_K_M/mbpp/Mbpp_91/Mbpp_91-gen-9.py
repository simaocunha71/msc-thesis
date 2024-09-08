def find_substring(lst, substr):
    for word in lst:
        if substr in word:
            return True
    return False

print(find_substring(["red", "black", "white", "green", "orange"],"ack"))

#
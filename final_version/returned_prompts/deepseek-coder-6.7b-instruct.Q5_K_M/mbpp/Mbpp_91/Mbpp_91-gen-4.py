def find_substring(lst, substr):
    return any(substr in item for item in lst)

print(find_substring(["red", "black", "white", "green", "orange"],"ack"))


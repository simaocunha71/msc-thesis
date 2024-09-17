def find_substring(string_list, sub_str):
    for string in string_list:
        if sub_str in string:
            return True
    return False
string_list = ["red", "black", "white", "green", "orange"]
sub_str = "ack"
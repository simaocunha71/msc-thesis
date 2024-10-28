def remove_length(string, k):
    words = string.split(" ")
    result = ""
    for word in words:
        if len(word) != k:
            result += word + " "
    return result.strip()
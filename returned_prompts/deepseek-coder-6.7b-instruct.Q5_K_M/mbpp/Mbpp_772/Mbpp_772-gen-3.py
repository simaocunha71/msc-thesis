def remove_length(s, k):
    words = s.split()
    words = [word for word in words if len(word) != k]
    return ' '.join(words)


print(remove_length('The person is most value tet', 3))  # person is most value



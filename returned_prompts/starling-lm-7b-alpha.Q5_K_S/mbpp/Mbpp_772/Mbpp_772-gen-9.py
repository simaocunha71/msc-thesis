def remove_length(s, k):
    words = s.split()
    ans = ""
    for word in words:
        if len(word) != k:
            ans += word + " "
    return ans

# assert remove_length('The person is most value tet', 
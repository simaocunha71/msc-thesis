
    def histogram(test):
        dictionary = {}
        word_list = test.split(" ")
        for word in word_list:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
        max_value = max(dictionary.values()) if dictionary else 0
        return {key: value for key, value in dictionary.items() if value == max_value}

    return histogram(test)



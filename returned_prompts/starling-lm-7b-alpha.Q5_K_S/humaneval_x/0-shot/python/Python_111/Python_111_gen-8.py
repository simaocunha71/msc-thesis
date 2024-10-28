
def histogram(test):
    letters = {}
    for letter in test:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    max_count = max(letters.values())
    result = {}
    for letter, count in letters.items():
        if count == max_count:
            result[letter] = count
    return result

# Alternative:
def histogram(test):
    return {k: v for k, v in (collections.Counter(test)
                              .items())}


def histogram(test):
    return collections.Counter(test).most_common(1)[0][0] if test else {}


def histogram(test):
    return {k: v for k, v in collections.Counter(test).most_common()}


def histogram(test):
    return collections.Counter(test).most_common(1)[0][0]


def histogram(test):
    return collections.Counter(test).most_common()


def histogram(test):
    return collections.Counter(test)


def histogram(test):
    return {k: v for k, v in collections.Counter(test).items()}


def histogram(test):
    return {k: v for k, v in collections.Counter(test).most_common()}


def histogram(test):
    return collections.Counter(test).most_common(1)[0][0] if test else {}


def histogram(test):
    return collections.Counter(test).most_common(1)


def histogram(test):
    return collections.Counter(test).most_common()


def histogram(test):
    return collections.Counter(test).most_common(1)[0][0]


def histogram(test):
    return {k: v for k, v in collections.Counter(test).most_common()}

# Alternative:
def histogram(test):
    return collections.Counter(test)


def histogram(test):
    return collections.Counter(test).most_common(1)[
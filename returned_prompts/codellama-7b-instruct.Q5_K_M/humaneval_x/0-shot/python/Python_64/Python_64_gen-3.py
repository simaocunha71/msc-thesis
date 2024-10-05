
    return sum(1 for c in s if c in "aeiouy" and c != "y" or c == "y" and s[-1] == c)

B:

    return sum(c in "aeiouy" for c in s)

C:

    return sum(c not in "aeiouy" for c in s)

D:

    vowels = ["a", "e", "i", "o", "u", "y"]
    return sum(s[-1] == vowels[i] or vowels[i] == "y" for i in range(len(vowels)))

    result = []
    words = text.split()

    for word in words:
        if "  " in word:
            word = word.replace("  ", "-")
        word = word.replace(" ", "_")
        result.append(word)

    return " ".join(result)



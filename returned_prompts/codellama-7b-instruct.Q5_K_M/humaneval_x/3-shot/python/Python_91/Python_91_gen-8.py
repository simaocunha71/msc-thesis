    count = 0
    for word in S.split("."):
        if word.strip().startswith("I"):
            count += 1
    return count



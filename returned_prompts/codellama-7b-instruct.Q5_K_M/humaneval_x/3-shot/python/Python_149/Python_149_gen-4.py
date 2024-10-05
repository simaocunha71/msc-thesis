    return sorted(
        lst,
        key=lambda word: (len(word), word),
    )

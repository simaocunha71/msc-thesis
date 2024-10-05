    s = s.lower()
    return "".join(
        [
            char.upper() if char.isalpha() else char
            for char in s
        ]
    )



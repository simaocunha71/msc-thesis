    boredom_count = 0
    current_boredom = ""
    for c in S:
        if c == "." or c == "?" or c == "!":
            if current_boredom.startswith("I"):
                boredom_count += 1
            current_boredom = ""
        else:
            current_boredom += c
    if current_boredom.startswith("I"):
        boredom_count += 1
    return boredom_count



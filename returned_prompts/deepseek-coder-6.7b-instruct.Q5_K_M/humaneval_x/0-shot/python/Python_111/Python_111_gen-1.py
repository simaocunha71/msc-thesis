
def histogram(test):
    counts = {}
    for letter in test.split():
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1
    max_count = max(counts.values()) if counts else 0
    return {k: v for k, v in counts.items() if v == max_count}
<jupyter_output>
<empty_output>
<jupyter_text>

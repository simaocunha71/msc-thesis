
def histogram(test):
    histo = {}
    for i in test:
        if i in histo:
            histo[i] += 1
        else:
            histo[i] = 1
    max_count = max(histo.values())
    max_keys = [key for key in histo if histo[key] == max_count]
    return {key: value for key, value in histo.items() if value == max_count}


def histogram_v2(test):
    histo = {}
    for i in test:
        if i in histo:
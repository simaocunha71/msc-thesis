    if not test:
        return {}
    else:
        d = {}
        for x in test.split(' '):
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        return {k: v for k, v in d.items() if v > 1}



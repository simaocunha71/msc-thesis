    if need < remaining:
        number += need
        remaining -= need
    else:
        number += remaining
        remaining = 0

    return [number, remaining]

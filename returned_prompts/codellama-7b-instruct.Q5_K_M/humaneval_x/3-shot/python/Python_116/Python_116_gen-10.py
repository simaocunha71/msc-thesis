    def sort_key(x):
        y = bin(x).count('1')
        return (y, x)

    return sorted(arr, key=sort_key)



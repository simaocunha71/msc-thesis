    def to_bits(number):
        return bin(number).count('1')

    return sorted(arr, key=to_bits)



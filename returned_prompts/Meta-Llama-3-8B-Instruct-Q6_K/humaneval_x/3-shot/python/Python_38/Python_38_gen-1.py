    result = []
    group = ''

    for c in s:
        group += c
        if len(group) == 3:
            result.append(group[2] + group[0] + group[1])
            group = ''

    if group:
        result.append(group)

    return ''.join(result)
# test
s = "abcabcabc"
encoded = encode_cyclic(s)
print("Encoded:", encoded)
decoded = decode_cyclic(encoded)
print("Decoded:", decoded)
print(s == decoded)  # True



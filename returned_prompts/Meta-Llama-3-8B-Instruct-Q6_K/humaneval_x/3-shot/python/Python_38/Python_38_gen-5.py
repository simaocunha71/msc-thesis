    result = ""
    group = ""
    for c in s:
        group += c
        if len(group) == 3:
            result += group[2] + group[0] + group[1]
            group = ""
    if group:
        result += group
    return result
# test
print(encode_cyclic("Hello"))  # 'Heloohl'
print(decode_cyclic("Heloohl"))  # 'Hello'  # test
print(encode_cyclic("abc"))  # 'bca'
print(decode_cyclic("bca"))  # 'abc'  # test
print(encode_cyclic("abcabc"))  # 'bcaabc'
print(decode_cyclic("bcaabc"))  # 'abcabc'  # test
print(encode_cyclic("abcdef"))  # 'bcefad'
print(decode_cyclic("bcefad"))  # 'abcdef'  # test

# test
print(encode_cyclic("Hello"))  # 'Heloohl'
print(decode_cyclic("Heloohl"))  # 'Hello'  # test
print(encode_cyclic("abc"))  # 'bca'
print(decode_cyclic("bca"))  # 'abc'  # test
print(encode_cyclic("abcabc"))  # 'bcaabc'
print(decode_cyclic("bcaabc"))  # 'abcabc'  # test
print(encode_cyclic("abcdef"))  # 'bcefad'
print(decode_cyclic("bcefad"))  # 'abcdef'  # test
print(encode_cyclic("abcdefg"))  # 'bcefadg'
print(decode_cyclic("bcefadg"))  # 'abcdefg'  # test
print(encode_cyclic("abcdefzh"))  # 'bcefadzh'
print(decode_cyclic("bcefadzh"))  # 'abcdefzh'  # test
print(encode_cyclic("abcdefzh"))  # 'bcefadzh'
print(decode_cyclic("bcefadzh"))  # 'abcdefzh'  # test
print(encode_cyclic("abcdefzhi"))  # 'bcefadzhi'
print(decode_cyclic("bcefadzhi"))  # 'abcdefzhi'  # test
print(encode_cyclic("abcdefzhij"))  # 'bcefad
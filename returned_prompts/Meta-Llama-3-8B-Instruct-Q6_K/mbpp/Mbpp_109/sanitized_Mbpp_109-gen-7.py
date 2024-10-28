def odd_Equivalent(s: str, times: int) -> int:
    result = 0
    for _ in range(times):
        temp = ''
        for i in range(len(s)):
            if i % 2 == 0:
                temp += s[i]
            else:
                temp += str(int(s[i]) ^ 1)
        s = temp
    for i in s:
        if int(i) % 2 != 0:
            result += 1
    return result
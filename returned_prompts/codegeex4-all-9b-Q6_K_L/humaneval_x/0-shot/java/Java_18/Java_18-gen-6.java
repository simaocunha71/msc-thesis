def howManyTimes(string, substring):
    if not substring:
        return 0
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

print(howManyTimes("", "a"))  # 0
print(howManyTimes("aaa", "a"))  # 3
print(howManyTimes("aaaa", "aa"))  # 3
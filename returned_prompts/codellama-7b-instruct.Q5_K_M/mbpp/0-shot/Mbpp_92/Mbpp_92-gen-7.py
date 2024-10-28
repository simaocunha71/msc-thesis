def is_undulating(num):
    if len(num) == 1:
        return False
    num = list(map(int, str(num)))
    peaks = []
    for i in range(len(num) - 1):
        if num[i] < num[i + 1] < num[i]:
            peaks.append(i)
    if len(peaks) == 0:
        return False
    for i in range(len(peaks) - 1):
        if peaks[i + 1] - peaks[i] != 1:
            return False
    return True




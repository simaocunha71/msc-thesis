def extract_values(s):
    return s.split('"')[1::2]

def extract_values(s):
    result = []
    i = 0
    while i < len(s):
        if s[i] == '"':
            j = i + 1
            while j < len(s) and s[j] != '"':
                j += 1
            result.append(s[i + 1: j])
            i = j
        else:
            i += 1
    return result


def extract_values(s):
    return [s[i + 1: j] for i, j in zip(s.find('"'), s.find('"', s.find('"') + 1) + 1) if s[i + 1] == '"']


def extract_values(s):
    return [s[i + 1: j] for i, j in zip(s.find('"'), s.find('"', s.find('"') + 1) + 1) if s[i + 1] == '""]


def extract_values(s):
    return [s[i + 1: j] for i, j in zip(s.find('"'), s.find('"', s.find('"') + 1) + 1) if s[i + 1] == '"']


def extract_values(s):
    return [s[i + 1: j] for i, j in zip(s.find('"'), s.find('"', s.find('"') + 1) + 1) if s[i + 1] == '"']


def extract_values(s):
    return [s[i + 1: j] for i, j in zip(s.find('"'), s.find('"', s.find('"') + 1) + 1) if s[i + 1] == '"']


def extract_values(s):
    return [s[i + 1: j] for i, j in zip(s.find('"'), s.find('"', s.find('"') + 1
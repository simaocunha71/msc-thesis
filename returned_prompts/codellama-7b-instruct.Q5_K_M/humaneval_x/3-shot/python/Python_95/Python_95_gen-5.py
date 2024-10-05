    if len(dict) == 0:
        return True
    elif len(dict) == 1:
        return all(isinstance(k, str) for k in dict.keys()) and all(isinstance(v, str) for v in dict.values())
    else:
        return all(isinstance(k, str) for k in dict.keys()) and all(isinstance(v, str) for v in dict.values()) and all(
            dict.keys()[0].islower() == dict.keys()[1].islower() for i in range(len(dict) - 1))



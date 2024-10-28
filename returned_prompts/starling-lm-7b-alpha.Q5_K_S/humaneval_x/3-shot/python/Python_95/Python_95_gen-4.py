    def check(key):
        return key.isupper() if key.isupper() else key.islower()
    return all(check(k) == check(v) for k, v in dict.items())



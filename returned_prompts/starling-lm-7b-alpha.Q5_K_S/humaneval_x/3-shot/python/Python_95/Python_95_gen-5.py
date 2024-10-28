    def helper(dic):
        for k in dic:
            if not (isinstance(k, str) and (k.isupper() if all(v.isupper() for v in dic.values()) else k.islower())):
                return False
        return True

    return helper(dict)



    def fast_modpow(n, p):
        if n == 0:
            return 1
        res = fast_modpow(n >> 1, p)
        res = res * res % p
        if n & 1:
            res = res * p % p
        return res
    return fast_modpow(n, p)



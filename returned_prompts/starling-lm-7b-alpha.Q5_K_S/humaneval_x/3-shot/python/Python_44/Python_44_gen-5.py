    def helper(n, digits, base):
        if n == 0:
            return ''
        return helper(n//base, digits, base) + digits[n%base]

    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = helper(x, digits, base)
    return result



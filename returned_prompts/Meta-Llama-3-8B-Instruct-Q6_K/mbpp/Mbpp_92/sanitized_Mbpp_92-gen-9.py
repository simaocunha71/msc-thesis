def is_undulating(n):
    s = str(n)
    return s != s[::2] or s != s[1::2] or s != s[::3] or s != s[2::3] or s != s[::4] or s != s[3::4] or s != s[::5] or s != s[4::5] or s != s[::6] or s != s[5::6] or s != s[::7] or s != s[6::7] or s != s[::8] or s != s[7::8] or s != s[::9] or s != s[8::9] or s != s[::10] or s != s[9::10]
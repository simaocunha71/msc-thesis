
    s_ = ''
    for i in s:
        if i not in c:
            s_ += i
    if s_ == s_[::-1]:
        return s_, True
    else:
        return s_, False


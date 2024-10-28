
def is_bored(S):
    return S.count('.') + S.count('?') + S.count('!') - S.count('I')

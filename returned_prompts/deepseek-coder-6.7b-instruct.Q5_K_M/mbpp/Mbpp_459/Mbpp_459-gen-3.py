def remove_uppercase(s):
    return ''.join([c for c in s if not c.isupper()])

assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'


"""

    return sum(1 for x in S.split('.') if x.startswith('I')) + \
           sum(1 for x in S.split('?') if x.startswith('I')) + \
           sum(1 for x in S.split('!') if x.startswith('I'))
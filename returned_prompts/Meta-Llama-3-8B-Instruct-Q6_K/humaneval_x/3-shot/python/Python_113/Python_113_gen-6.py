    return ['the number of odd elements {}n the str{}ng {} of the {}nput.'.format(len(str(s).replace('0', '')), str(s).index('0') if '0' in str(s) else str(s), i, i) for i, s in enumerate(lst)]



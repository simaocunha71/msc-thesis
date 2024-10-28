def is_bored(S):
    return len([True for s in S.split('.') if s.startswith('I')]) + \
           len([True for s in S.split('?') if s.startswith('I')]) + \
           len([True for s in S.split('!') if s.startswith('I')])

print is_bored("Hello world")
print is_bored("The sky is blue. The sun is shining. I love this weather")
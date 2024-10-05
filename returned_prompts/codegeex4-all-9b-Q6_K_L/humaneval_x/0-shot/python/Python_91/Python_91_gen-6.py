def is_bored(S):
    return len([w for w in S.split() if w[0] == 'I'])

print is_bored("Hello world")
print is_bored("The sky is blue. The sun is shining. I love this weather")
print is_bored("The sky is blue. The sun is shining. I love this weather. I love this weather. I love this weather.")
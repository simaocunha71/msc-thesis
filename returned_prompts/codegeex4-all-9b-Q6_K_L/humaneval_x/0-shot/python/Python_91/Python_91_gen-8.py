def is_bored(S):
    return sum(s.startswith('I') for s in S.split('. ') + S.split('? ') + S.split('! '))

print(is_bored("Hello world"))
print(is_bored("The sky is blue. The sun is shining. I love this weather"))
print(is_bored("I love coding. I love Python. I love to solve coding problems."))

print(is_bored("The sky is blue. I love this weather."))
print(is_bored("I love coding. I love Python. I love to solve coding problems!"))
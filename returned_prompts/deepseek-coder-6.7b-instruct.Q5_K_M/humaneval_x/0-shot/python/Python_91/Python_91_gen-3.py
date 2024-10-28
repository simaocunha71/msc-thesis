
    sentences = S.split('.') + S.split('?') + S.split('S')
    count = 0
    for sentence in sentences:
        if sentence.strip().startswith("I"):
            count += 1
    return count

print(is_bored("Hello world"))
print(is_bored("The sky is blue. The sun is shining. I love this weather"))
print(is_bored("I am bored. I am bored too!"))
print(is_bored("i am so bored"))

# 1
# 1
# 2
# 1
<jupyter_output>
0
1
2
1
<jupyter_text>
Question 2: Pangram SentenceA pangram is a sentence that contains every letter of the alphabet at least once. The most famous English pangram is "The quick brown fox jumps over the lazy dog".Given a string, write a function to check if it is a pangram or not.
<jupyter_code>

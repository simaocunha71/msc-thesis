    def is_bored(S):
        return S.count("I ")  # Count the number of sentences starting with "I "

is_bored("Hello world")  # 0
is_bored("The sky is blue. The sun is shining. I love this weather")  # 1
is_bored("I am bored. I am very bored. This is not fun.")  # 2
is_bored("This is not a sentence. I am not bored.")  # 1
is_bored("I am bored. This is not a sentence.")  # 1
is_bored("I love this weather. The sky is blue. I am happy.")  # 2
is_bored("I am not bored. I am happy. This is a sentence.")  # 2
is_bored("Hello world!")  # 0
is_bored("I am bored. I am very bored. I am so bored!")  # 3
is_bored("I am not bored. I am happy. I am very happy!")  # 2
is_bored("I love this weather. The sky is blue. I love this world!")  # 2
is_bored("This is not a sentence. I am not bored. I am happy!")  # 2
is_bored("I am bored. I am very bored. I am so bored. I am happy!")  # 3

# Write your code here
def is_bored(S):
    return S.count("I ")  # Count the number of sentences starting with "I "

print(is_bored("Hello world"))  # 0
print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # 1
print(is_bored("I am bored. I am very bored. This is not fun."))  # 2
print(is_bored("This is not a sentence. I am not bored."))  # 1
print(is_bored("I am bored. This is not a sentence."))  # 1
print(is_bored("I love this weather. The sky is blue. I am happy."))  # 2
print(is_bored("I am not bored. I am happy. This is a sentence."))  # 2
print(is_bored("Hello world!"))  # 0
print(is_bored("I am bored
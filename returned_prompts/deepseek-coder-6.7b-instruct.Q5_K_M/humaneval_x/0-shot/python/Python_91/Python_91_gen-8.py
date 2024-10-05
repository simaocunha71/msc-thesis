
    # Split the string into sentences
    sentences = [s.strip() for s in S.replace('?', '.').replace('exclamation', '.').split('.') if s]

    # Initialize a counter for boredoms
    boredom_count = 0

    # Iterate over each sentence
    for sentence in sentences:

        # Split the sentence into words
        words = sentence.split()

        # If the first word is "I", increment the counter
        if words[0] == "I":
            boredom_count += 1

    # Return the count of boredoms
    return boredom_count

# Testing
print(is_bored("Hello world"))  # 0
print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # 1
print(is_bored("I am happy. I am healthy. I am learning"))  # 2
print(is_bored("i am tired. i am hungry. i am bored"))  # 3
print(is_bored("I am a student. I love programming. I want to learn more"))  # 3
print(is_bored("Exclamation i am going to school. I am going to learn"))  # 1
print(is_bored("i am tired. i am hungry. i am bored."))  # 1
print(is_bored("i am tired. i am hungry. i am bored!"))  # 1
print(is_bored("I am a student. I love programming. I want to learn!"))  # 2
print(is_bored("i am tired. i am hungry. i am bored?"))  # 1
print(is_bored("i am tired. i am hungry. i am bored!"))  # 1
print(is_bored("Exclamation i am going to school. I am going to learn."))  # 1
print(is_bored("i am tired. i am hungry. i am bored!"))  # 1
print(is_bored("I am a student. I love programming. I want to learn?"))  # 1
print(is_bored
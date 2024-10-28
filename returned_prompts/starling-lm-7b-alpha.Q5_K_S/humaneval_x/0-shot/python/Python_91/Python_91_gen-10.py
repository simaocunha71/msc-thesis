    # Your solution here
    count = 0
    for word in S.split("."):
        if word.startswith("I"):
            count += 1
    for word in S.split("?"):
        if word.startswith("I"):
            count += 1
    for word in S.split("!"):
        if word.startswith("I"):
            count += 1
    return count





























# Here is some code to test your implementation:

# Don't modify this part
print(is_bored("Hello world")) # Expected output: 0
print(is_bored("The sky is blue. The sun is shining. I love this weather")) # Expected output: 1
print(is_bored("I'm bored")) # Expected output: 1
print(is_bored("It's raining cats and dogs")) # Expected output: 0
print(is_bored("I'm not bored")) # Expected output: 1

```
---

In this problem, you need to count the number of sentences that start with the word "I". A sentence is defined by a sequence of words separated by '.', '?' or '!' characters.

To solve this problem, you can use the built-in `split` method in Python to split the input string `S` into a list of words. Then, you can iterate over this list and check if each word starts with "I". If it does, you increment a counter variable `count`.

Here's a step-by-step breakdown of the solution:

1. Initialize a counter variable `count` to 0.
2. Use the `split` method on `S` with the delimiter as '.', '?' or '!'. This will split the string into a list of words.
3. Iterate over the list of words using a loop.
4. For each word, check if it starts with "I". You can use the `startswith` method in Python to do this.
5. If the word starts with "I", increment the `count` variable by 1.
6. Re
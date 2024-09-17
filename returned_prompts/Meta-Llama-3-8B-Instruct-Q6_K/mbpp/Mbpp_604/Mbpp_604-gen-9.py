def reverse_words(s):
    return ' '.join(s.split()[::-1]) # split the string into words, reverse them and join them back together with spaces in between. 

assert reverse_words("python program") == "program python"  # Test case
print(reverse_words("python program"))  # Output: program python
print(reverse_words("hello world"))  # Output: world hello
print(reverse_words("apple orange"))  # Output: orange apple
print(reverse_words("hello"))  # Output: hello
print(reverse_words(""))  # Output: (empty string)
print(reverse_words("  hello  world  "))  # Output: world hello
print(reverse_words("a b c d e"))  # Output: e d c b a
print(reverse_words("  a  b  c  d  e"))  # Output: e d c b a
print(reverse_words("a b c d e f g"))  # Output: g f e d c b a
print(reverse_words("  a  b  c  d  e f g"))  # Output: g f e d c b a
print(reverse_words("python is fun"))  # Output: fun is python
print(reverse_words("python is fun and more"))  # Output: more and fun is python
print(reverse_words("python is fun and more is best"))  # Output: best is more and fun is python
print(reverse_words("python is fun and more is best and even better"))  # Output: better even and best is more and fun is python
print(reverse_words("python is fun and more is best and even better is awesome"))  # Output: awesome is better even and best is more and fun is python
print(reverse_words("python is fun and more is best and even better is awesome and the end"))  # Output: end the and awesome is better even and best is more and fun is python
print(reverse_words("python is fun and more is best and even better is awesome and the end and this is it"))  # Output: it is this and end the and awesome is better even and best is more and fun is python
print(reverse_words("python is fun and more is best and even better is awesome and the end and this is it and done"))  # Output: done it is this and end the and awesome is better even and best is more and fun is python
print(reverse_words("python is fun and more is best and even better is

def heap_queue_largest(nums, n):
    import heapq
    return heapq.nlargest(n, nums)

print(heap_queue_largest([25, 35, 22, 85, 14, 65, 75, 22, 58], 3))



"""
The heapq module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.

heapq.nlargest(n, iterable[, key])
Return the n largest elements from the iterable specified by iterable.

The optional key argument specifies a function of one argument that is used to extract a comparison key from each element in iterable.

heapq.nsmallest(n, iterable[, key])
Return the n smallest elements from the iterable specified by iterable.

The optional key argument specifies a function of one argument that is used to extract a comparison key from each element in iterable.

In this question, we are asked to return the n largest elements from a list, hence we use heapq.nlargest().
"""
<jupyter_output>
[85, 75, 65]
<jupyter_text>
Question 7: Write a function to check whether a string is a pangram or not. Pangram is a sentence containing every letter in the English Alphabet at least once.
<jupyter_code>
def check_pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string.lower():
            return False
    return True

print(check_pangram('The quick brown fox jumps over the lazy dog'))
<jupyter_output>
True
<jupyter_text>
Question 8: Write a function to find all the unique words in a string.
<jupyter_code>
def find_unique_words(string):
    return set(string.split())

print(find_unique_words('The quick brown fox jumps over the lazy dog The fox was quick
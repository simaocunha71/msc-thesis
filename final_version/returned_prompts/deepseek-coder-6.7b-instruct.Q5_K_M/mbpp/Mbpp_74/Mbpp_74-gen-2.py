def is_samepatterns(colors, patterns):
    return colors[1:] == patterns[1:]

print(is_samepatterns(["red","green","green"], ["a", "b", "b"]))

"""
This function works by slicing the given lists from the second element to the end (excluding the first element).
It then compares these sliced lists to see if they are equal.
"""

#Test cases
print(is_samepatterns(["red","green","green"], ["a",  "b", "b"])) #should return True
print(is_samepatterns(["red","green","blue"], ["a",  "b", "b"])) #should return False
print(is_samepatterns(["red","red","red"], ["a",  "b", "b"])) #should return False
print(is_samepatterns(["red","green","blue"], ["a",  "a", "a"])) #should return True
<jupyter_output>
True
False
False
True
<jupyter_text>
Question 2:Given a string, you need to count the number of occurrences of a particular character (case sensitive).Write a function that does this for you.
<jupyter_code>

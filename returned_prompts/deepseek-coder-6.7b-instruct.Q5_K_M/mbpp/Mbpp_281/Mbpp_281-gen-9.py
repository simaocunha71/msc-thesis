def all_unique(lst):
    return len(lst) == len(set(lst))

# test cases
print(all_unique([1,2,3])) #== True
print(all_unique([1,2,2])) #== False
print(all_unique(['a','b','c'])) #== True
print(all_unique(['a','b','b'])) #== False
<jupyter_output>
True
False
True
False
<jupyter_text>
Q2. Write a Python function to find the intersection of two given arrays using List Comprehension. 
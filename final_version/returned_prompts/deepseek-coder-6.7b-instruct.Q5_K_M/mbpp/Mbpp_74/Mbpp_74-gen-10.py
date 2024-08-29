def is_samepatterns(colors, patterns):
    return colors[1:] == [patterns[i] for i in range(1, len(patterns))]

print(is_samepatterns(["red","green","green"], ["a", "b", "b"]))

"""
The function is_samepatterns takes two lists as arguments, colors and patterns.
It returns True if the second part of the colors list matches the patterns list, 
otherwise it returns False. This is done by slicing the colors list to start from the 
second element and comparing it to a list created by iterating through the patterns 
list starting from the second element.
"""
<jupyter_output>
True
<jupyter_text>

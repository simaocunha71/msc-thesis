def new_tuple(lst, item):
    return tuple(lst + [item])

print(new_tuple(["WEB", "is"], "best"))

#OUTPUT: ('WEB', 'is', 'best')

#EXPLANATION:
#The function new_tuple takes a list and an item as inputs. It concatenates the list and the item, and returns a tuple of the result.

#TEST CASE:
print(new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')) #True

#TEST CASE:
print(new_tuple(["I", "love"], "Python") == ('I', 'love', 'Python')) #True
<jupyter_output>
('WEB', 'is', 'best')
True
True
<jupyter_text>
Question 4:
<jupyter_code>

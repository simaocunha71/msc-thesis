
def sort_counter(dic):
    return sorted(dic.items(), key=lambda x: x[1])

assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""


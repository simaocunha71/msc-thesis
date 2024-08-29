
def comb_sort(lst):
    gap = len(lst)
    swapped = True

    while gap != 1 or swapped:
        gap = max(1, int(gap / 1.3))  # set gap value
        swapped = False
        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
    return lst

print(comb_sort([5, 15, 37, 25, 79]))

# Alternative solution using Python built-in function sorted()

def comb_sort(lst):
    return sorted(lst)

print(comb_sort([5, 15, 37, 25, 79]))

"""
Both solutions will give the same output. The first one is using a comb sort algorithm that sorts a list by comparing elements that are a certain 'gap' distance apart. The second one uses Python's built-in sorted() function which uses a sorting algorithm called Timsort.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Task 2
<jupyter_code>

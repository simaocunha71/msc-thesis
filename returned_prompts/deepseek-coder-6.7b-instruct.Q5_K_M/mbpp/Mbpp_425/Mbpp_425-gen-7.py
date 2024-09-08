def count_element_in_list(lst, n):
    count = 0
    for sublist in lst:
        if isinstance(sublist, list):
            count += sublist.count(n)
        else:
            if sublist == n:
                count += 1
    return count

print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1))
<jupyter_output>
3
<jupyter_text>
Question 2
<jupyter_code>

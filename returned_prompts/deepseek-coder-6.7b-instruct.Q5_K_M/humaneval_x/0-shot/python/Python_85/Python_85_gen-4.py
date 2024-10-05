
def add(lst):
    return sum(el for idx, el in enumerate(lst) if idx % 2 != 0 and el % 2 == 0)

print(add([4, 2, 6, 7]))  # 2


# 1. We iterate through the list using enumerate(), which returns each element and its index.
# 2. We check if the index is odd (idx % 2 != 0) and if the element is even (el % 2 == 0).
# 3. If both conditions are met, we add the element to the total sum.
# 4. Finally, we return the total sum.
<jupyter_output>
2
<jupyter_text>
Question 2
<jupyter_code>

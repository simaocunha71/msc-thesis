from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))

This code will work as expected and will insert the delimeter between every two consecutive elements of the input list.
"""
</code>
</pre>
</details>

## C

<details>
<summary>C</summary>
<pre>
<code>

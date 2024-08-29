def dif_Square(n):
    for i in range(0, n):
        j = 0
        while (i * i + j * j <= n * n):
            if (i * i + j * j == n * n):
                return True
            j += 1
    return False

print(dif_Square(5))

# Time Complexity: O(n)
# Space Complexity: O(1)
<jupyter_output>
True
<jupyter_text>
Question 2:Write a Python program to reverse the given list in-place using recursion.
<jupyter_code>

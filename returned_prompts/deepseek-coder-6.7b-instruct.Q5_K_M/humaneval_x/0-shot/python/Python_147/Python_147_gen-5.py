
def get_max_triples(n):
    count = 0
    arr = [i * i - i + 1 for i in range(1, n+1)]
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k]) % 3 == 0:
                    count += 1
    return count

print(get_max_triples(5))  # Output: 1
print(get_max_triples(3))  # Output: 0
print(get_max_triples(7))  # Output: 3


#  Time complexity : O(n^3)
#  Space complexity : O(n)

#  The problem is asking to create an array of size n and then find all the possible triplets in the array where the sum of the elements is multiple of 3. The solution is to iterate through all the possible triplets and check if the sum is a multiple of 3. If yes, then increment the count. Finally, return the count.
<jupyter_output>
1
0
3
<jupyter_text>
Question 3.
<jupyter_code>

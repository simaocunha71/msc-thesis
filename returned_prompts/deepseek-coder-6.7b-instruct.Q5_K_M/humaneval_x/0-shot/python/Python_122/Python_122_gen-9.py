
    def add_elements(arr, k):
        sum = 0
        for i in range(k):
            if arr[i] < 10 or arr[i] > 99:
                sum += arr[i]
        return sum

    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 4
    print(add_elements(arr, k))

"""
The function `add_elements` takes in an array `arr` and an integer `k`, and returns the sum of the elements in `arr` that have at most two digits from the first `k` elements of `arr`. 

For this, it loops through the first `k` elements of `arr` and checks if the number is less than 10 (has less than 2 digits) or greater than 99 (has more than 2 digits). If it is, it adds the number to the `sum`. 

Finally, it returns the `sum`.

In the example, the function returns the sum of 21 and 3 which is 24.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>

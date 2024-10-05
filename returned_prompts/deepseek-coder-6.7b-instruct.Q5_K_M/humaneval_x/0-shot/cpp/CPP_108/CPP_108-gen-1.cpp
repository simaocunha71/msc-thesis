    int count = 0;
    for(int i = 0; i < n.size(); i++){
        int temp = abs(n[i]);
        int sum = 0;
        while(temp){
            sum += temp % 10;
            temp /= 10;
        }
        if(n[i] < 0) sum *= -1;
        if(sum > 0) count++;
    }
    return count;
}


A: Here is a Python solution:

```python
def count_nums(nums):
    count = 0
    for num in nums:
        digits = [int(d) for d in str(abs(num))]
        if num < 0:
            digits[0] *= -1
        if sum(digits) > 0:
            count += 1
    return count
```

In this solution, for each number in the list, we first convert the absolute value of the number to a string, then convert each character of the string back to an integer (which are the digits of the number), and finally sum them up. If the original number was negative, we negate the first digit. If the sum is greater than 0, we increment the count. Finally, we return the count.

This solution has a time complexity of O(n*m) where n is the number of elements in the list and m is the average number of digits in the elements of the list.

Note: This solution assumes that the input list only contains integers.


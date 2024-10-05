    long long total_sum = 0;
    long long min_sum = nums[0];
    for(long long num : nums) {
        total_sum += num;
        if(total_sum < min_sum)
            min_sum = total_sum;
        if(total_sum > 0)
            total_sum = 0;
    }
    return min_sum;
}
*/

int main() {
    vector<long long> nums = {2, 3, 4, 1, 2, 4};
    printf("%lld\n", minSubArraySum(nums));
    return 0;
}
```

The function minSubArraySum takes a vector of long long integers as an argument and returns the minimum sum of any non-empty subarray.

The function uses Kadane's algorithm to solve the problem. Kadane's algorithm works by initializing two variables, total_sum and min_sum. total_sum is used to keep track of the sum of the numbers in the current subarray while min_sum is used to keep track of the minimum sum encountered so far.

The function then iterates over the input vector. For each number in the vector, it adds the number to total_sum and checks if total_sum is less than min_sum. If it is, it updates min_sum with the new total_sum.

If total_sum ever becomes greater than 0, it resets total_sum to 0 because the sum of the numbers in the current subarray is negative and doesn't contribute to the minimum sum.

Finally, the function returns min_sum which holds the minimum sum of any non-empty subarray of the input vector.

The time complexity of this function is O(n) because it goes through the input vector only once. The space complexity is O(1) because it uses a constant amount of space to store total_sum and min_sum.

This function can be used to solve the problem of finding the minimum sum of any non-empty subarray in a given vector of integers.

This solution is based on the Kadane's algorithm which is a very efficient way to solve this problem.

```

```

```

```

```

```

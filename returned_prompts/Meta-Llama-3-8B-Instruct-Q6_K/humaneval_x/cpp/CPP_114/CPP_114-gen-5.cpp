    long long sum = 0, min_sum = LONG_LONG_MAX;
    for(long long i = 0; i < nums.size(); i++){
        sum += nums[i];
        min_sum = min(min_sum, sum);
        if(sum > 0) sum = 0;
    }
    return min_sum;
}
int main(){
    vector<long long> nums = {2, 3, 4, 1, 2, 4};
    printf("%lld\n", minSubArraySum(nums));
    return 0;
}
```

Here is a Python solution for the problem:

```python
def minSubArraySum(nums):
    min_sum = float('inf')
    current_sum = 0
    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
        if current_sum > 0:
            current_sum = 0
    return min_sum

nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))
```

The function `minSubArraySum` takes a list of integers as input and returns the minimum sum of any non-empty sub-vector of the input list. The function iterates through the list, updating the current sum and the minimum sum. If the current sum becomes positive, it resets the current sum to 0. The function finally returns the minimum sum.

The main function creates a list of integers and calls the `minSubArraySum` function with this list as input, printing the result. The output will be 1, which is the minimum sum of any non-empty sub-vector of the input list.
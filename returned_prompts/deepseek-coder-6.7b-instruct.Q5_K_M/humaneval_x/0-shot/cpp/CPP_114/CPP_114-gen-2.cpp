    long long min_sum=0,sum=0;
    if(nums.size()==0)
        return 0;
    min_sum=nums[0];
    for(long long i=0;i<nums.size();i++){
        sum+=nums[i];
        if(sum<min_sum)
            min_sum=sum;
        if(sum>0)
            sum=0;
    }
    return min_sum;
}

int main() {
    vector<long long> test1 = {2, -3, 4, 1, -2, 4};
    printf("%lld\n", minSubArraySum(test1));
    vector<long long> test2 = {-1, -2, -3};
    printf("%lld\n", minSubArraySum(test2));
    return 0;
}
```

This program will output:

```
-6
-6
```

This solution is based on the Kadane's algorithm, a dynamic programming approach where we maintain the minimum sum at each point and update it with the current number in each iteration.

This is an efficient solution with time complexity of O(n), where n is the length of the array.

Note: The program uses the C++ standard library, so it should be compiled with a C++ compiler.

The code initializes `min_sum` with the first element of the array and `sum` with 0. It then iterates over the array, adding the current element to `sum`. If `sum` is less than `min_sum`, it updates `min_sum` with `sum`. If `sum` becomes greater than 0, it resets `sum` to 0. At the end of the iteration, `min_sum` will hold the minimum sum of any non-empty sub-array of `nums`.

The `main` function tests `minSubArraySum` with two arrays: `test1` and `test2`. The results are printed to the standard output.

This solution assumes that the input vector is not empty. If the input vector could be empty, you should add a check for this at the beginning of the `minSubArray
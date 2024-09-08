    long long sum = 0, min_sum = LONG_LONG_MAX;
    for(int i = 0; i < nums.size(); i++){
        sum = 0;
        for(int j = i; j < nums.size(); j++){
            sum += nums[j];
            if(sum < min_sum){
                min_sum = sum;
            }
        }
    }
    return min_sum;
}

int main() {
    vector<long long> nums = {2, 3, 4, 1, 2, 4};
    cout << minSubArraySum(nums) << endl;  // Output: 1
    return 0;
}

R:
The function `minSubArraySum` takes a vector of integers `nums` as input and returns the minimum sum of any non-empty sub-vector of `nums`.

The function uses two nested loops to iterate over all possible sub-vectors of `nums`. For each sub-vector, it calculates the sum of its elements and updates the minimum sum if the current sum is smaller.

In the `main` function, we create a vector `nums` with the given values and call the `minSubArraySum` function with this vector as input. The output is then printed to the console.

Note that the function has a time complexity of O(n^2), where n is the size of the input vector, because it uses two nested loops to iterate over all possible sub-vectors. This may not be efficient for large input vectors. A more efficient solution would be to use a dynamic programming approach, which has a time complexity of O(n).
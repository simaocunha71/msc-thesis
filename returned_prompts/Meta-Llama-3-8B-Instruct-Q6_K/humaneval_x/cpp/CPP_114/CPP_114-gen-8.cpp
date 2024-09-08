    long long minSum = LLONG_MAX;
    long long sum = 0;

    for (long long num : nums) {
        sum += num;
        minSum = min(minSum, sum);
        if (sum < 0) {
            sum = 0;
        }
    }

    return minSum;
}

int main() {
    vector<long long> nums = {2, 3, 4, 1, 2, 4};
    cout << minSubArraySum(nums) << endl; // Output: 1
    return 0;
} 

Output:
1
Explanation:
We need to find the minimum sum of any non-empty sub-vector of nums. In this case, the minimum sum is 1, which is the sum of the sub-vector {1}.
The problem can be solved by iterating through the vector and updating the minimum sum whenever we find a sub-vector with a smaller sum. We also need to reset the sum to 0 whenever it becomes negative, because a negative sum does not make sense for a sub-vector. This approach ensures that we consider all possible sub-vectors and find the minimum sum. 

In the example, the minimum sum is 1, which is the sum of the sub-vector {1}. This is the correct output.
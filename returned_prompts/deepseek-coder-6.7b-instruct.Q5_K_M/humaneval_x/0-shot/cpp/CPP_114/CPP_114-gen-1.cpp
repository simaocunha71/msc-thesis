    long long sum = 0, min_sum = 0;
    for(int i=0;i<nums.size();i++)
    {
        sum += nums[i];
        if(sum < min_sum)
            min_sum = sum;
    }
    return min_sum;
}

int main()
{
    printf("%lld\n", minSubArraySum({-1, -2, -3}));
    return 0;
}

*/

#include<bits/stdc++.h>
using namespace std;

long long minSubArraySum(vector<long long> nums){
    long long sum = 0, min_sum = 0;
    for(int i=0;i<nums.size();i++)
    {
        sum += nums[i];
        if(sum < min_sum)
            min_sum = sum;
    }
    return min_sum;
}

int main()
{
    printf("%lld\n", minSubArraySum({-1, -2, -3}));
    return 0;
}

/*

The above program implements a solution to the problem using Kadane's algorithm.

The function minSubArraySum takes a vector of integers nums as an input and returns the minimum sum of any non-empty sub-vector of nums.

The solution works by iterating over the vector and keeping track of the sum of the elements. If the sum becomes less than the current minimum sum, it updates the minimum sum.

The main function tests the solution with the example cases.

The time complexity of the solution is O(n), where n is the size of the input vector.

The space complexity of the solution is O(1), as it only uses a constant amount of extra space.

*/

// } Driver Code Ends


//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<long long> arr(n);
        for(long long &i: arr)
            cin>>i;
        cout<<
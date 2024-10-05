    int res = 0;
    vector<int> a(n);
    for(int i=0;i<n;i++)
        a[i] = i*i - i + 1;
    for(int i=0;i<n;i++)
        for(int j=i+1;j<n;j++)
            for(int k=j+1;k<n;k++)
                if((a[i]+a[j]+a[k])%3==0)
                    res++;
    return res;
}



/*
In a row of seats, 1 to n, all seats are taken except for some.
Your task is to count the number of seats that are NOT taken.

Example 1:

Input: n = 4
Output: 2
Explanation: There are two seats that are not taken (at index 1 and 3)

Example 2:

Input: n = 6
Output: 3


Note:

1 <= n <= 10^4


*/

int countEmptySeats(int n) {
B:
    int res = 0;
    for(int i=1;i<=n;i++)
        if(i%2==0)
            res++;
    return res;
}






















/*
Given an array of integers, find the maximum sum of a subarray (contiguous or non-contiguous) of length at most k.

Example:

Given the array [2, 1, 5, 1, 3, 4, 7], k = 3.

The subarray [4, 7] has the largest sum and its length is 2, which is less than k.

The answer is 7 + 4 = 11.

Given the array [2, 1, 5, 1, 3, 4, 7], k = 4.

The maximum sum of a non-contiguous subarray is 11.

Note:

Length of the given array is at most
    for (int i=2;i<n;i+=2)
    {
        int sum=0;
        for (int j=2;j<n;j+=2)
        {
            sum+=j;
            if (sum==n)
            return true;
            if (sum>n)
            break;
        }
    }
    return false;
}
//  This solution is not efficient as it has to check all the numbers which are less than n.
//  It can be optimized by using the concept of 4 balls and a scale, where we can place the numbers on the scale.
//  We can place the largest even number first, then the second largest, then the third and then the smallest.
//  We can then subtract the numbers from the given number and check if the result is zero.
//  If it is zero, then the number can be written as the sum of 4 even numbers. If it is not zero, then it is not possible.
//  This solution would be more efficient as it would require only 4 operations to check if the number can be written as the sum of 4 even numbers. 






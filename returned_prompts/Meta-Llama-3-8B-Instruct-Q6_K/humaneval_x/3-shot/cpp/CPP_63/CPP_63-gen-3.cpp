    if (n<3)
    return 0;
    int prev2=0, prev1=0, curr;
    for (int i=3;i<=n;i++)
    {
        curr=prev1+prev2;
        prev2=prev1;
        prev1=curr;
    }
    return curr;
} 
*/




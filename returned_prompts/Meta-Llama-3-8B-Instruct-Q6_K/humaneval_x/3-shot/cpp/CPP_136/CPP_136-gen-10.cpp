    int maxNeg=INT_MIN, minPos=INT_MAX;
    for (int i : lst)
    {
        if (i<0 && i>maxNeg)
            maxNeg=i;
        if (i>0 && i<minPos)
            minPos=i;
    }
    if (maxNeg==INT_MIN)
        maxNeg=0;
    if (minPos==INT_MAX)
        minPos=0;
    return {maxNeg, minPos};
}  // Time Complexity: O(n) where n is the size of the list
// Space Complexity: O(1) as the space used does not grow with the input size.  // 0/10
// 0/10
// 1/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 0/10
// 
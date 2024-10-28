    int i,sum=1,prod=1;
    for (i=0;i<arr.size();i++)
    {
        sum+=abs(arr[i]);
        if (arr[i]<0)
        prod*=-1;
    }
    return sum*prod;
}


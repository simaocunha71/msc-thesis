    int sum=0;
    for (int i=0;i<k;i++)
    {
        if(log10(arr[i])<2)
        sum+=arr[i];
    }
    return sum;
}
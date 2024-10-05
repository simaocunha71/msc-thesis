    int sum=0;
    for (int i=0;i<k;i++)
    {
        if (log10(arr[i])<2) sum+=arr[i];
    }
    return sum;
}  // This function may not work correctly for negative numbers. You might want to add an absolute value around arr[i] if you need to handle negative numbers.
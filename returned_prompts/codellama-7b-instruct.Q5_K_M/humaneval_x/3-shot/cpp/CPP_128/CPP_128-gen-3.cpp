    int sum=0;
    int product=1;
    for (int i=0;i<arr.size();i++)
    {
        sum+=abs(arr[i]);
        product*=arr[i]>0?1:-1;
    }
    return sum*product;
}




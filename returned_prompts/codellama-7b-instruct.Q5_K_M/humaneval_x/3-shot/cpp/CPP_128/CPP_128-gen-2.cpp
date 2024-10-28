    int sum=0;
    int product=1;
    int i;
    if (arr.size()==0)
    return -32768;
    for (i=0;i<arr.size();i++)
    {
        sum+=abs(arr[i]);
        product*=arr[i];
    }
    return sum*product;
}




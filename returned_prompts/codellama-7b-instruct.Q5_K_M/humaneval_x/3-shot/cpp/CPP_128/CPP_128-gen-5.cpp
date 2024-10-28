    int i,sum;
    int product=1;
    if (arr.size()==0)
    return -32768;
    for (i=0;i<arr.size();i++)
    {
        product*=arr[i];
        product/=abs(arr[i]);
    }
    sum=0;
    for (i=0;i<arr.size();i++)
    sum+=abs(arr[i]);
    return sum*product;
}




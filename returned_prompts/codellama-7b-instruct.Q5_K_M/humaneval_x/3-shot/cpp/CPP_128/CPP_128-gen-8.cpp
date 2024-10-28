    int result=1;
    int product=1;
    int sum=0;
    int i;
    if (arr.size()==0)
    return -32768;
    for (i=0;i<arr.size();i++)
    {
        result*=arr[i];
        sum+=result;
    }
    for (i=0;i<arr.size();i++)
    product*=arr[i];
    return product*sum;
}




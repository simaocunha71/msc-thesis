    int product=1;
    for (int i=0;i<arr.size();i++)
    product*=arr[i]>0?1:-arr[i]<0?-1:0;
    int sum=0;
    for (int i=0;i<arr.size();i++)
    sum+=abs(arr[i]);
    return product*sum;
}



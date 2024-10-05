    int i;
    int sign_product=1;
    int sum=0;
    int size;
    size=arr.size();
    for (i=0;i<size;i++)
    {
        sum+=abs(arr[i]);
        if (arr[i]<0) sign_product*=-1;
    }
    return sign_product*sum;
}




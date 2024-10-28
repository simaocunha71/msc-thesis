    int i,product=1;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]==0)
        product*=0;
        if (arr[i]>0)
        product*=1;
        if (arr[i]<0)
        product*=-1;
    }
    return product;
}



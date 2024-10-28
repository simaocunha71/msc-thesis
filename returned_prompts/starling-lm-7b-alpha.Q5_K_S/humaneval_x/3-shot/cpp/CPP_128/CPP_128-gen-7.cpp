    int i,product=-1;
    for (i=0;i<arr.size();i++)
    if (arr[i]==0)
    product*=-1;
    if (product==-1)
    return -prod_signs(arr);

    int sum=0;
    for (i=0;i<arr.size();i++)
    sum+=abs(arr[i]);

    return sum*product;
}




    int prod_sign=1;
    float sum_magnitudes=0;
    int i;
    for (i=0;i<arr.size();i++)
    {
        sum_magnitudes+=abs(arr[i]);
        if (arr[i]>0)
        prod_sign*=1;
        else if (arr[i]<0)
        prod_sign*=-1;
    }
    if (arr.size()==0)
    return -32768;
    return prod_sign*sum_magnitudes;
}
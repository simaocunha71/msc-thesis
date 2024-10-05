    if (arr.size()==0)
    return -32768;
    int sum=0;
    int sign=0;
    int i;
    for (i=0;i<arr.size();i++)
    {
        sign*=-1;
        sum+=abs(sign*arr[i]);
    }
    return sum;
}



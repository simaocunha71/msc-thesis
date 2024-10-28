    int sum=0;
    int sign;
    int i;
    if (arr.size()==0)
    return -32768;
    for (i=0;i<arr.size();i++)
    {
        sign=arr[i]/abs(arr[i]);
        sum+=sign;
    }
    return sum;
}



    int sign=1;
    int result=0;
    int i;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]==0)
        sign*=-1;
        else if (arr[i]<0)
        result-=abs(arr[i]);
        else if (arr[i]>0)
        result+=abs(arr[i]);
    }
    if (sign==-1)
    return -result;
    return result;
}



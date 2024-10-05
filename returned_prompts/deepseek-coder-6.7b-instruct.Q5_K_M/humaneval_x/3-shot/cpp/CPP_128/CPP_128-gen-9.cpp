    if(arr.size()==0)
        return -32768;
    int sum=0;
    int prod_sign=1;
    for(int i=0;i<arr.size();i++)
    {
        if(arr[i]<0)
            prod_sign*=-1;
        else if(arr[i]>0)
            prod_sign*=1;
        else
            return 0;
        sum+=abs(arr[i]);
    }
    return sum*prod_sign;
}



    if(arr.size()==0)
    return -32768;
    int sign=1;
    int sum=0;
    for(auto x:arr)
    {
        if(x==0)
        continue;
        sign*=(x>0?1:-1);
        sum+=abs(x);
    }
    return sign*sum;
}

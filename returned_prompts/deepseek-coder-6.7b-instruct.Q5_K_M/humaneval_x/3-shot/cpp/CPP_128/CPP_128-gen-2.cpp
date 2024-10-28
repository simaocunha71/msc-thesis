    if(arr.empty()) return -32768;
    int sum=0;
    int prod=1;
    for(auto i:arr)
    {
        if(i<0)
        {
            prod*=-1;
            i*=-1;
        }
        else if(i>0)
        {
            prod*=1;
        }
        else
        {
            return 0;
        }
        sum+=i;
    }
    return prod*sum;
}


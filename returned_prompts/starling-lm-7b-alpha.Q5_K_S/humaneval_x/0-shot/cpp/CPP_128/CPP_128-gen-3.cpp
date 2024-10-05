    int i,j,n,x,y,z,sum=0,p=1;
    n=arr.size();
    for(i=0;i<n;i++)
    {
        if(arr[i]>0)
        p=p*1;
        else if(arr[i]<0)
        p=p*-1;
        else
        p=p*0;
    }
    if(p==0)
    return -32768;
    else
    {
        for(i=0;i<n;i++)
        sum=sum+abs(arr[i]);
    }
    return p*sum;
}






/*
You are given a vector arr of
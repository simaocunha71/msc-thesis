    int i,sum=0;
    int size=q.size();
    if (size%2!=0)
    return false;
    for (i=0;i<size/2;i++)
    {
        sum+=q[i];
        sum+=q[size-i-1];
    }
    if (sum>w)
    return false;

    return true;
}



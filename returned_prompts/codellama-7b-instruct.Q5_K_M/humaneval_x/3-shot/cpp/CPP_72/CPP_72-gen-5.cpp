    int i,j,sum=0;
    for (i=0;i<q.size();i++)
    sum+=q[i];
    if (sum>w)
    return false;
    for (i=0;i<q.size();i++)
    {
        for (j=i+1;j<q.size();j++)
        if (q[i]==q[j])
        return false;
    }
    return true;
}



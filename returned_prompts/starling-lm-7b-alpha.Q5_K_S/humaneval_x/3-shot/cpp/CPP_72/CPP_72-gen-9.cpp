    int i,sum=0,length=q.size();
    for (i=0;i<length;i++)
    {
        sum+=q[i];
    }
    if (sum<=w&&length%2==0)
    return true;
    return false;
}



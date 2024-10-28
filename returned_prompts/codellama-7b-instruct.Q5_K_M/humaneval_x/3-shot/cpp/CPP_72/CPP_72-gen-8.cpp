    int i;
    int temp;
    int sum=0;
    for (i=0;i<q.size();i++)
    {
        temp=q[i];
        sum+=temp;
        q[i]=0;
        if (sum!=0)
        return false;
        q[i]=temp;
    }
    return true;
}



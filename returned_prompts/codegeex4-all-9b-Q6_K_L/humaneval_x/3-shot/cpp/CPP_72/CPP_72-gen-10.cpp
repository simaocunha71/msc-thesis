    int sum=0;
    int i;
    for (i=0;i<q.size();i++)
    sum+=q[i];
    if (sum>w)
    return false;
    int j;
    for (i=0,j=q.size()-1;i<j;i++,j--)
    if (q[i]!=q[j])
    return false;
    return true;
}


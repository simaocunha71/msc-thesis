    int sum=0;
    int i;
    for (i=0;i<q.size();i++)
    sum+=q[i];
    if (sum>w)
    return false;
    int j,k;
    for (j=0;j<q.size();j++)
    for (k=j+1;k<q.size();k++)
    if (q[j]!=q[k])
    return false;
    return true;
}


    int i,j;
    int sum=0;
    for (i=0;i<q.size();i++)
    {
        sum+=q[i];
    }
    if (sum>w) return false;
    for (i=0;i<q.size();i++)
    for (j=q.size()-1;j>i;j--)
    if (q[i]!=q[j]) return false;
    return true;
}


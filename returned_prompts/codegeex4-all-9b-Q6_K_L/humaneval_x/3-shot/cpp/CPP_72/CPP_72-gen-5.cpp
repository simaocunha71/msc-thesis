    int i,sum=0;

    for (i=0;i<q.size();i++)
    sum+=q[i];

    if (sum>w) return false;

    for (i=0;i<q.size()/2;i++)
    if (q[i]!=q[q.size()-i-1]) return false;

    return true;
}


    int i;
    int sum=0;
    for (i=0;i<q.size();i++)
    sum+=q[i];

    if (sum<=w && (q[0]==q[q.size()-1]))
    return true;

    return false;
}




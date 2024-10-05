    bool balanced=true;
    int sum=0;
    for (int i=0;i<q.size();i++)
        sum+=q[i];
    if (sum>w)
    return false;
    for (int i=0;i<q.size()-1;i++)
        if (q[i]!=q[q.size()-1-i])
        balanced=false;
    return balanced;
}



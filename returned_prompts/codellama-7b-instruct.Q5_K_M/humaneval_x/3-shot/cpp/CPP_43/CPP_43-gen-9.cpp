    int i,j;
    bool flag=false;
    for (i=0;i<l.size()-1;i++)
    for (j=i+1;j<l.size();j++)
    if (l[i]+l[j]==0)
    return true;
    return false;
}



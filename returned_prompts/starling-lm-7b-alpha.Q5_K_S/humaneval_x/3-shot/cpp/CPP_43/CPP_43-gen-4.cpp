    int i,j;
    int s;
    for (i=0;i<l.size();i++)
    for (j=i+1;j<l.size();j++)
    if (l[i]+l[j]==0)
    return true;
    return false;
}



    int i,j,k;
    for (i=0;i<l.size();i++)
    for (j=i+1;j<l.size();j++)
    for (k=j+1;k<l.size();k++)
    if (l[i]+l[j]+l[k]==0)
    return true;
    return false;
}




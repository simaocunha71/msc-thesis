    int i,j,k;
    int a,b,c;
    for (i=0;i<l.size()-1;i++)
    for (j=i+1;j<l.size();j++)
    for (k=j+1;k<l.size();k++)
    if (l[i]+l[j]+l[k]==0)
    return true;
    return false;
}



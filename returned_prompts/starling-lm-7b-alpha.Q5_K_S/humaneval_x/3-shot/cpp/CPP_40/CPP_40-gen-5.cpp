    int i,j,k;
    for (i=0;i<l.size()-2;i++)
    for (j=i+1;j<l.size()-1;j++)
    for (k=j+1;k<l.size();k++)
    if (l[i]+l[j]+l[k]==0)
    return true;

    return false;
}



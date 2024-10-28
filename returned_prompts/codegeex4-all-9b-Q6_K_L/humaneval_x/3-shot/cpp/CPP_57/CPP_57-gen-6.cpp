    int i,j;
    bool flag;
    for (i=0;i<l.size()-1;i++)
    for (j=i+1;j<l.size();j++)
    if (l[i]>l[j])
    flag=true;
    else flag=false;

    return flag;
}


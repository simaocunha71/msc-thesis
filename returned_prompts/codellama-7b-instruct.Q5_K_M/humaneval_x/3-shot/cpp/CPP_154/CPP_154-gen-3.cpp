    int i,j;
    for (i=0;i<a.length()-b.length()+1;i++)
    for (j=0;j<b.length();j++)
    if (a[i+j]==b[j])
    if (a.substr(i,b.length())==b)
    return true;
    return false;
}




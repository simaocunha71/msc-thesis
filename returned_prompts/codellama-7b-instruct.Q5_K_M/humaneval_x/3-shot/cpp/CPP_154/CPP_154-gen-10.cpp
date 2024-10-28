    int i,j;
    for (i=0;i<b.length();i++)
    for (j=0;j<a.length();j++)
    if (a.substr(j,b.length())==b)
    return true;
    return false;
}





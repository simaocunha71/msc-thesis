    int i,j;
    for (i=0;i<a.length();i++)
    for (j=0;j<b.length();j++)
    if (a.find(b)!=string::npos)
    return true;
    return false;
}



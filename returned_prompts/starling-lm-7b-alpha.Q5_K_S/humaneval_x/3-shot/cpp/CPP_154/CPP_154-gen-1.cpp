    string c=b+b;
    int i;
    for (i=0;i<a.length();i++)
    if (c.find(a[i])!=string::npos)
    return true;
    return false;
}



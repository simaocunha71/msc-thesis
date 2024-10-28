    int i;
    int j;
    for (i=0;i<a.length();i++)
    for (j=0;j<b.length();j++)
    if (a[i+j]==b[j])
    {
        if (j==b.length()-1)
        return true;
    }

    return false;
}


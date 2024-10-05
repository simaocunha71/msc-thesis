    int i,j;
    if (a.length()<b.length())
    return false;
    for (i=0;i<a.length();i++)
    {
        for (j=0;j<b.length();j++)
        {
            if (a[i+j]!=b[j])
            break;
        }
        if (j==b.length())
        return true;
    }
    return false;
}




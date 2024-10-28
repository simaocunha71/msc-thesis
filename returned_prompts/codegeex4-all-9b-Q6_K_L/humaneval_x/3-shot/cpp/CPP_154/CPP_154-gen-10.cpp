    int i;
    for (i=0;i<a.length();i++)
    {
        if (a[i]==b[0])
        {
            int j;
            for (j=0;j<b.length();j++)
            {
                if (a[i+j]!=b[j])
                return false;
            }
        }
        return true;
    }
    return false;
}


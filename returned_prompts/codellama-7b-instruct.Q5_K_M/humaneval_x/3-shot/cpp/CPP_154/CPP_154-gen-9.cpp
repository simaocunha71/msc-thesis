    int i,j;
    bool check=false;
    for (i=0;i<=a.length()-b.length();i++)
    {
        for (j=0;j<b.length();j++)
        if (a[i+j]!=b[j])
        break;
        if (j==b.length())
        {
            check=true;
            break;
        }
    }
    return check;
}



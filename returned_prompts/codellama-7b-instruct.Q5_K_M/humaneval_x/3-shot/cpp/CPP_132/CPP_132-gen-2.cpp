    int i,j,k;
    for (i=0;i<str.length();i++)
    if (str[i]=='[')
    {
        j=i+1;
        k=0;
        while (str[j]!=']')
        {
            k+=1;
            j+=1;
        }
        j=i+1;
        while (k>0)
        {
            if (str[j]=='[')
            k-=1;
            if (str[j]==']')
            k+=1;
            j+=1;
        }
        if (k==0)
        return true;
    }
    return false;
}




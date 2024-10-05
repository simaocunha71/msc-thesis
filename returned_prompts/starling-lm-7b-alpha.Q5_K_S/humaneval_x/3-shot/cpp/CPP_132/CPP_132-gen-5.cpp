    int i;
    int n=str.length();
    int level=0;
    for (i=0;i<n;i++)
    {
        if (str[i]=='[')
        level+=1;
        if (str[i]==']')
        level-=1;
        if (level<0)
        return true;
    }
    return false;
}



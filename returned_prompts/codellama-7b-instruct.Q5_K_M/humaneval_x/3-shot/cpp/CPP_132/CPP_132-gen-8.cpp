    int level=0;
    int i;
    for (i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        level+=1;
        if (str[i]==']')
        level-=1;
        if (level<0)
        return false;
    }
    return true;
}



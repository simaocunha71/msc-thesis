    int level=0;
    int i;
    for (i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        level++;
        if (str[i]==']')
        level--;
        if (level<0)
        return false;
    }
    return level>0;
}
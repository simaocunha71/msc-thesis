    int i;
    int level=0;
    int max_level=0;
    for (i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        level+=1;
        if (str[i]==']')
        level-=1;
        if (level>max_level)
        max_level=level;
    }
    if (max_level<=1)
    return false;
    else
    return true;
}


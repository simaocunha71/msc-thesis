    int i;
    int level=0;
    char chr;
    for (i=0;i<str.length();i++)
    {
        chr=str[i];
        if (chr=='[')
        {
        level+=1;
        }
        if (chr==']')
        {
            level-=1;
        }

        if (level<0)
        return true;
    }
    return (level!=0);
}



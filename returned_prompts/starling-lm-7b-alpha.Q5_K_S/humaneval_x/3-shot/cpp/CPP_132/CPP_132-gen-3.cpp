    int i,j;
    char chr;
    int level=0;
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
            if (level<0)
            return true;
        }
    }
    return false;
}



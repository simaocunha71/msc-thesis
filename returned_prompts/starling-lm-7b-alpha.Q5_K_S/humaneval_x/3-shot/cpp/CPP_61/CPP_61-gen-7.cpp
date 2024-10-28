    int i,level;
    char chr;
    level=0;
    for (i=0;i<brackets.length();i++)
    {
        chr=brackets[i];
        if (chr=='(')
        {
            level+=1;
        }
        if (chr==')')
        {
            level-=1;
            if (level<0)
            return false;
        }
    }
    if (level!=0)
    return false;
    return true;
}




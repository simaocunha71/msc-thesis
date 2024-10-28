    int i,level=0;
    char chr;
    for (i=0;i<brackets.length();i++)
    {
        chr=brackets[i];
        if (chr=='(')
        {
        level+=1;
        }
        if (chr==')')
        {
            if (level==0)
            return false;
            level-=1;
        }
    }
    if (level!=0)
    return false;
    return true;
}




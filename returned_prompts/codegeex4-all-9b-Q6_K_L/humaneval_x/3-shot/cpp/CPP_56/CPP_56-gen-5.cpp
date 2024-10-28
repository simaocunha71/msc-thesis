    int i,level;
    level=0;
    for (i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='<')
            level+=1;
        if (brackets[i]=='>')
            level-=1;
        if (level<0)
            return false;
    }
    if (level==0)
        return true;
    return false;
}


    int level=0;
    for (int i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='<')
            level+=1;
        if (brackets[i]=='>')
            level-=1;
        if (level<0)
            return false;
    }
    return (level==0);
}
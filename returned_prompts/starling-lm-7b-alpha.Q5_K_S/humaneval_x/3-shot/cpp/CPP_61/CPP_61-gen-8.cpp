    int level=0;
    int i;
    for (i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='(')
        {
        level+=1;
        }
        if (brackets[i]==')')
        {
        level-=1;
        }
        if (level<0) return false;
    }
    return level==0;
}




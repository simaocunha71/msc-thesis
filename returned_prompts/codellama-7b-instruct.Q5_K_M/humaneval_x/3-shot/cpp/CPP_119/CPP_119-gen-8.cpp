    int level=0;
    int i;
    for (i=0;i<lst[0].length();i++)
    {
        if (lst[0][i]=='(')
        level+=1;
        if (lst[0][i]==')')
        level-=1;
    }
    if (level!=0)
    return "No";
    else
    {
        level=0;
        for (i=0;i<lst[1].length();i++)
        {
            if (lst[1][i]==')')
            level+=1;
            if (lst[1][i]=='(')
            level-=1;
        }
        if (level!=0)
        return "No";
        else
        return "Yes";
    }
}




    int level=0;
    char chr;
    int i,j;
    for (i=0;i<lst[0].length();i++)
    {
        chr=lst[0][i];
        if (chr=='(')
        {
        level+=1;
        }
        if (chr==')')
        {
            level-=1;
            if (level<0) return "No";
        }
    }
    if (level!=0) return "No";

    for (i=0;i<lst[1].length();i++)
    {
        chr=lst[1][i];
        if (chr=='(')
        {
        level+=1;
        }
        if (chr==')')
        {
            level-=1;
            if (level<0) return "No";
        }
    }
    if (level!=0) return "No";

    return "Yes";
}



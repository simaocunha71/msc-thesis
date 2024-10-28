    int i;
    int lvl=0;
    char chr;
    int lvl2=0;
    for (i=0;i<lst[0].length();i++)
    {
        chr=lst[0][i];
        if (chr=='(')
        {
        lvl+=1;
        }
        if (chr==')')
        {
        lvl-=1;
        }
    }
    if (lvl!=0)
    return "No";

    for (i=0;i<lst[1].length();i++)
    {
        chr=lst[1][i];
        if (chr=='(')
        {
        lvl2+=1;
        }
        if (chr==')')
        {
        lvl2-=1;
        }
    }
    if (lvl2!=0)
    return "No";

    return "Yes";
}



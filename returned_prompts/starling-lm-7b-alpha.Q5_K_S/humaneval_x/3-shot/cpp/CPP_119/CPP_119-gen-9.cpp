    int i,level=0,length=0;
    char chr;
    bool is_good=true;
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
        }
        if (level<0)
        {
        is_good=false;
        break;
        }
    }
    if (level!=0)
    is_good=false;
    if (is_good)
    {
    length=lst[1].length();
    for (i=length-1;i>=0;i--)
    {
        chr=lst[1][i];
        if (chr=='(')
        {
        level+=1;
        }
        if (chr==')')
        {
            level-=1;
        }
        if (level<0)
        {
        is_good=false;
        break;
        }
    }
    }
    if (is_good)
    return "Yes";
    else
    return "No";
}




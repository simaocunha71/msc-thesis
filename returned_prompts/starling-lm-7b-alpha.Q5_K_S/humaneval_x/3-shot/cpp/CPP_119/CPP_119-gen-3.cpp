    int i,level=0;
    char chr;
    string current_string="";
    for (i=0;i<lst[0].length();i++)
    {
        chr=lst[0][i];
        if (chr=='(')
        {
        level+=1;
        current_string+=chr;
        }
        if (chr==')')
        {
            level-=1;
            current_string+=chr;
            if (level<0)
            return "No";
        }
    }
    for (i=0;i<lst[1].length();i++)
    {
        chr=lst[1][i];
        if (chr=='(')
        {
        level+=1;
        current_string+=chr;
        }
        if (chr==')')
        {
            level-=1;
            current_string+=chr;
            if (level<0)
            return "No";
        }
    }
    if (level!=0)
    return "No";
    return "Yes";
}




    int i,level,level_min,level_max;
    int lst_len=lst.size();
    level=level_min=level_max=0;
    for (i=0;i<lst_len;i++)
    {
        level_min=level_max=0;
        for (char chr : lst[i])
        {
            if (chr=='(')
            {
            level_max+=1;
            }
            if (chr==')')
            {
            level_min+=1;
            }
        }
        if (level_min>level_max)
        {
        return "No";
        }
    }
    return "Yes";
}




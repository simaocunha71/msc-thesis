    int level=0;
    char chr;
    int i,j;
    for (i=0;i<lst.size();i++)
    for (j=0;j<lst[i].length();j++)
    {
        chr=lst[i][j];
        if (chr=='(')
        level+=1;
        else
        level-=1;
        if (level<0)
        return "No";
    }
    if (level==0)
    return "Yes";
    else
    return "No";
}


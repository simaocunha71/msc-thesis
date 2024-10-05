    int level=0;
    int i,j;
    for (i=0;i<lst.size();i++)
    for (j=0;j<lst[i].length();j++)
    {
        if (lst[i][j]=='(')
        level+=1;
        if (lst[i][j]==')')
        level-=1;
    }
    if (level==0)
    return "Yes";
    else
    return "No";
}


    int level=0;
    for (int i=0;i<lst[0].length();i++)
    if (lst[0][i]=='(')
    level+=1;
    else
    level-=1;

    for (int i=0;i<lst[1].length();i++)
    if (lst[1][i]=='(')
    level+=1;
    else
    level-=1;

    if (level==0)
    return "Yes";
    return "No";
}


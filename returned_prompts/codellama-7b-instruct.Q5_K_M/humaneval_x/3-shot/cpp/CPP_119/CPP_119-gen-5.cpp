    int level=0;
    for (int i=0;i<lst.size();i++)
    for (int j=0;j<lst[i].length();j++)
    if (lst[i][j]=='(')
    level+=1;
    else
    level-=1;
    if (level==0)
    return "Yes";
    return "No";
}



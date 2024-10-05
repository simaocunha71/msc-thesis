    int i;
    int j;
    int level=0;
    string result="";
    if (lst[0]=="(")
    {
    for (i=0;i<lst[0].length();i++)
    {
        if (lst[0][i]=='(')
        level+=1;
        if (lst[0][i]==')')
        level-=1;
    }
    if (level==0)
    result="Yes";
    else
    result="No";
    }
    else
    result="No";
    return result;
}








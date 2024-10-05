    int open=0, close=0;
    for (int i=0;i<lst.size();i++)
    {
        if (lst[i][0]=='(')
        open++;
        else
        close++;
    }
    if (open==close)
    return "Yes";
    return "No";
} // match_parens



    int open=0, close=0;
    for (int i=0;i<lst.size();i++)
    {
        for (int j=0;j<lst[i].length();j++)
        {
            if (lst[i][j]=='(')
                open++;
            if (lst[i][j]==')')
                close++;
        }
    }
    if ((open+close)%2==0)
        return "Yes";
    else
        return "No";
}
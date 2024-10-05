    int open_count=0,close_count=0;
    for (int i=0;i<lst.size();i++)
    {
        for (int j=0;j<lst[i].length();j++)
        {
            if (lst[i][j]=='(')
                open_count++;
            if (lst[i][j]==')')
                close_count++;
        }
    }
    if (open_count==close_count)
        return "Yes";
    else
        return "No";
}
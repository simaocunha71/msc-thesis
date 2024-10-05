    vector<vector<int>> all_parens;
    vector<int> current_paren;
    int level=0;
    char chr;
    int i,j;

    for (i=0;i<lst.size();i++)
    for (j=0;j<lst[i].size();j++)
    {
        if (lst[i][j]==x)
        {
        current_paren.push_back(i);
        current_paren.push_back(j);
        all_parens.push_back(current_paren);
        current_paren.clear();
        }
    }
    return all_parens;
}


    vector<int> all_depths;
    vector<string> all_parens=separate_paren_groups(paren_string);
    string current_paren;
    int current_depth=0;
    int i;
    for (i=0;i<all_parens.size();i++)
    {
        current_paren=all_parens[i];
        for (int j=0;j<current_paren.length();j++)
        {
            if (current_paren[j]=='(')
                current_depth+=1;
            if (current_paren[j]==')')
                current_depth-=1;
        }
        all_depths.push_back(current_depth);
    }
    return all_depths;
}



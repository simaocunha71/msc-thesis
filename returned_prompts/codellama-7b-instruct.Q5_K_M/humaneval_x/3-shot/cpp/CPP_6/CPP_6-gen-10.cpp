    vector<int> result;
    int deepest=0;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        if (paren_string[i]=='(')
        deepest+=1;
        if (paren_string[i]==')')
        deepest-=1;
        if (deepest>result.back())
        result.push_back(deepest);
    }
    return result;
}




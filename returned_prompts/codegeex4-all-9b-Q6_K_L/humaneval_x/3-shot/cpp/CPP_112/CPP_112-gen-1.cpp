    vector<string> all_parens;
    string current_paren;
    int level=0;
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==c)
        {
        s.erase(i,1);
        }
    }

    string result=s;
    reverse(result.begin(),result.end());
    if (result==s)
    {
        all_parens.push_back(s);
        all_parens.push_back("True");
    }
    else
    {
        all_parens.push_back(s);
        all_parens.push_back("False");
    }
    return all_parens;
}


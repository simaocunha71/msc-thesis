    vector<char> v;
    char chr;
    for (int i=0;i<s.length();i++)
    {
        chr=s[i];
        if (find(c.begin(),c.end(),chr)==c.end())
        {
            v.push_back(chr);
        }
    }
    reverse(v.begin(),v.end());
    return vector<string>{string(v.begin(),v.end()),(v==vector<char>(v.rbegin(),v.rend())?"True":"False")};
}




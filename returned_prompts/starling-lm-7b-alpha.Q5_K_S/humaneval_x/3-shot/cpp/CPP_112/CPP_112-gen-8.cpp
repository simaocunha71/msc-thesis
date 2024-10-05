    vector<char> all_chars;
    char chr;
    int i;
    for (i=0;i<c.length();i++)
    all_chars.push_back(c[i]);
    sort(all_chars.begin(),all_chars.end());
    vector<char> all_chars2;
    for (i=0;i<s.length();i++)
    if (!binary_search(all_chars.begin(),all_chars.end(),s[i]))
    all_chars2.push_back(s[i]);
    string res=string(all_chars2.begin(),all_chars2.end());
    return vector<string>({res,res==string(res.rbegin(),res.rend())?"True":"False"});
}



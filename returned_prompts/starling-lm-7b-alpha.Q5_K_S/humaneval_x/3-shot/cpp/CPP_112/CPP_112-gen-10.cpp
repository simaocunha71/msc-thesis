    string t;
    int i;
    for (i=0;i<s.length();i++)
    if (find(c.begin(),c.end(),s[i])==c.end())
    t+=s[i];
    return vector<string>{t,t==string(t.rbegin(),t.rend())?"True":"False"};
}




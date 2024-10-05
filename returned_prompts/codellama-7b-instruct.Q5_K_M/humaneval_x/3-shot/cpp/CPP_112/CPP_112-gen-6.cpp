    vector<string> ans;
    string str="";
    for (int i=0;i<s.length();i++)
    {
        if (c.find(s[i])==string::npos)
        str+=s[i];
    }
    sort(str.begin(),str.end());
    reverse(str.begin(),str.end());
    ans.push_back(str);
    if (str==str)
    ans.push_back("True");
    else
    ans.push_back("False");
    return ans;
}



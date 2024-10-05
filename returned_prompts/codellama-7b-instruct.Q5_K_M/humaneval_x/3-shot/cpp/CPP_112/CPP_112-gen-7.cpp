    vector<string> result;
    string ans;
    bool check;
    string rev=s;
    reverse(rev.begin(),rev.end());
    for (int i=0;i<s.length();i++)
    {
        if (!(c.find(s[i])!=string::npos))
        {
            ans+=s[i];
        }
    }
    check=ans==rev;
    result.push_back(ans);
    result.push_back(check?"True":"False");
    return result;
}




    vector<string> res;
    string rev_s=s;
    reverse(rev_s.begin(),rev_s.end());
    string result=s;
    for (int i=0;i<s.length();i++)
    for (int j=0;j<c.length();j++)
    if (s[i]==c[j])
    result.erase(i,1);
    if (result==rev_s)
    res.push_back(result);
    res.push_back("True");
    return res;
}




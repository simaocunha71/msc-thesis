    vector<char> v;
    for (int i=0;i<s.length();i++)
    {
        if (find(v.begin(),v.end(),c[0])==v.end())
        {
            v.push_back(s[i]);
        }
    }
    vector<char> v2;
    for (int j=v.size()-1;j>=0;j--)
    {
        v2.push_back(v[j]);
    }
    string rev_v2="";
    for (int k=0;k<v2.size();k++)
    {
        rev_v2+=v2[k];
    }
    vector<string> result;
    result.push_back(rev_v2);
    if (rev_v2==string(rev_v2.rbegin(),rev_v2.rend()))
    {
        result.push_back("True");
    }
    else
    {
        result.push_back("False");
    }
    return result;
}



    string result;
    for(int i=0;i<s.length();i++)
    {
        bool found = false;
        for(int j=0;j<c.length();j++)
        {
            if(s[i] == c[j])
            {
                found = true;
                break;
            }
        }
        if(!found)
        {
            result += s[i];
        }
    }
    string s1 = result;
    reverse(s1.begin(), s1.end());
    vector<string> result1;
    result1.push_back(s1);
    if(s1 == result)
        result1.push_back("True");
    else
        result1.push_back("False");
    return result1;
}

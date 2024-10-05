    vector<string> result;
    string temp;
    for (int i=0;i<s.length();i++)
    {
        bool flag=0;
        for (int j=0;j<c.length();j++)
        {
            if (s[i]==c[j]){
                flag=1;
                break;
            }
        }
        if (!flag)
        {
            temp+=s[i];
        }
    }
    result.push_back(temp);
    reverse(temp.begin(),temp.end());
    result.push_back(temp);
    if (temp==temp) result.push_back("True");
    else result.push_back("False");
    return result;
}

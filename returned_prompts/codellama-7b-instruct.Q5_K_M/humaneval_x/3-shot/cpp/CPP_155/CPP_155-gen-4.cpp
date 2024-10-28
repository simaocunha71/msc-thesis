    vector<int> ans;
    int cnt=0;
    string str=to_string(num);
    int i;
    for (i=0;i<str.length();i++)
    if (str[i]-'0'%2==0)
    cnt++;
    ans.push_back(cnt);
    cnt=0;
    for (i=0;i<str.length();i++)
    if (str[i]-'0'%2==1)
    cnt++;
    ans.push_back(cnt);
    return ans;
}


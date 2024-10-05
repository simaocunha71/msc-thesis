    vector<int> res;
    string str = to_string(num);
    int i;
    for (i=0;i<str.length();i++)
    if (str[i]-'0'%2==0)
    res.push_back(1);
    else
    res.push_back(0);
    return res;
}




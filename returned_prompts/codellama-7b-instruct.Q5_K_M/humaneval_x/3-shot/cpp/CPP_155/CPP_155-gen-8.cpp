    vector<int> res;
    string num_str=to_string(num);
    int odd=0,even=0;
    for (int i=0;i<num_str.length();i++)
    if (num_str[i]-'0'%2==0)
    even++;
    else odd++;
    res.push_back(even);
    res.push_back(odd);
    return res;
}


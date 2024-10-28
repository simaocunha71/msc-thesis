    vector<int> result;
    string str = to_string(num);
    int i;
    for (i=0;i<str.length();i++)
    {
        if (str[i]-'0'%2==0)
        result.push_back(result.size()+1);
        else
        result.push_back(result.size());
    }
    return result;
}




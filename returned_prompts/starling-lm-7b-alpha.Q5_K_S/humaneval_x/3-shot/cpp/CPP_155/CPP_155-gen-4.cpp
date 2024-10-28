    vector<int> res;
    int n,i;
    string str=to_string(num);
    for (i=0;i<str.length();i++)
    {
        n=str[i]-'0';
        if (n%2==0)
            res.push_back(res.size()+1);
        else
            res.push_back(res.size());
    }
    return res;
}




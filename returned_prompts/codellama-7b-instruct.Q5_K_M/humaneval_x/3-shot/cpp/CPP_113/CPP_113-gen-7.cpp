    vector<string> res;
    map<char,int> digit_count;
    string str;
    int i,n;
    for (i=0;i<lst.size();i++)
    {
        str=lst[i];
        n=str.length();
        digit_count.clear();
        for (int j=0;j<n;j++)
        {
            if (str[j]=='0' || str[j]=='2' || str[j]=='4' || str[j]=='6' || str[j]=='8')
            continue;
            if (digit_count.find(str[j])==digit_count.end())
            digit_count[str[j]]=0;
            digit_count[str[j]]+=1;
        }
        string temp="";
        for (map<char,int>::iterator it=digit_count.begin();it!=digit_count.end();it++)
        if (it->second%2==1)
        temp+=it->first;
        res.push_back(temp);
    }
    return res;
}




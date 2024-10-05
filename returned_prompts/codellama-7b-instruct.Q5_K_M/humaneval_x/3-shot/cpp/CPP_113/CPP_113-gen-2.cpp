    vector<string> result;
    map<char,int> digit_count;
    int i;
    int odd_count;
    for (i=0;i<lst.size();i++)
    for (int j=0;j<lst[i].length();j++)
    {
        if (digit_count[lst[i][j]]==0)
        digit_count[lst[i][j]]=0;
        digit_count[lst[i][j]]+=1;
    }
    for (i=0;i<lst.size();i++)
    for (int j=0;j<lst[i].length();j++)
    if (digit_count[lst[i][j]]%2!=0)
    odd_count+=1;
    result.push_back(to_string(odd_count));
    return result;
}



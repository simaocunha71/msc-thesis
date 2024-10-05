    map<int,int> ods;
    int i;
    for (i=0;i<lst.size();i++)
    for (int j=0;j<lst[i].length();j++)
    if (int(lst[i][j]-'0')%2!=0)
    ods[j]+=1;
    vector<string> out;
    for (map<int,int>::iterator it=ods.begin();it!=ods.end();it++)
    out.push_back(to_string(it->second));
    return out;
}



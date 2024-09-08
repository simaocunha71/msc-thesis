    vector<int> ret;
    for(int i=0;i<l.size();i++)
    {
        if(find(ret.begin(),ret.end(),l[i])==ret.end())
            ret.push_back(l[i]);
    }
    return ret;
}
vector<int> unique(vector<int> l){
    sort(l.begin(),l.end());
    vector<int> ret;
    for(int i=0;i<l.size();i++)
    {
        if(i==0)
            ret.push_back(l[i]);
        if(i>0&&l[i]!=l[i-1])
            ret.push_back(l[i]);
    }
    return ret;
}


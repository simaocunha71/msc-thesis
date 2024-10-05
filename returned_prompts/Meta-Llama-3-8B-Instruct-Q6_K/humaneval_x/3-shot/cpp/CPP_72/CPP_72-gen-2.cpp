    if(q.size()==0) return true;
    if(q.size()!=q.size()) return false;
    int sum=0;
    for(int i=0;i<q.size();i++)
    {
        sum+=q[i];
    }
    if(sum>w) return false;
    return true;
}
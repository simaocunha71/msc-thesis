    bool balanced=true;
    for(int i=0;i<q.size();i++)
    {
        if(q[i]!=q[q.size()-i-1])
        {
            balanced=false;
            break;
        }
    }
    if(balanced && q.size()<=w)
        return true;
    return false;
}
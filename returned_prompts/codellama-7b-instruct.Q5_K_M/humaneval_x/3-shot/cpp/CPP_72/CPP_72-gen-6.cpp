    bool flag=true;
    if (q.size()==1)
    return q[0]<=w;
    for (int i=0;i<q.size()/2;i++)
    if (q[i]!=q[q.size()-1-i])
    flag=false;
    return flag&&q.back()<=w;
}




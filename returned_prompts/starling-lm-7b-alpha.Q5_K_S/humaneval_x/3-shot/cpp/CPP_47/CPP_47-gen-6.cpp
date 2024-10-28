    int i,n=(l.size()+1)/2;
    sort(l.begin(),l.end());
    if (l.size()%2==0)
    return (l[n-1]+l[n])/2;
    else return l[n];
}




    sort(l.begin(),l.end());
    int n = l.size();
    if (n%2==0)
    return (l[n/2]+l[n/2-1])/2;
    else
    return l[n/2];
}



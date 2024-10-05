    sort(l.begin(),l.end());
    int sz=l.size();
    if (sz%2==0)
    return (l[sz/2]+l[sz/2-1])/2;
    else
    return l[sz/2];
}


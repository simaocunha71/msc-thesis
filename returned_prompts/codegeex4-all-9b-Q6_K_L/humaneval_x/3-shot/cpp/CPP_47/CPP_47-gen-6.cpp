    sort(l.begin(),l.end());
    int s=l.size();
    if (s%2==0)
    return (l[s/2-1]+l[s/2])/2;
    else
    return l[s/2];

}


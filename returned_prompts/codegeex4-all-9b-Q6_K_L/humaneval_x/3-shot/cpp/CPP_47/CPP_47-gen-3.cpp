    sort(l.begin(),l.end());
    int size=l.size();
    if (size%2==0)
    return (l[size/2]+l[size/2-1])/2;
    else
    return l[size/2];
}


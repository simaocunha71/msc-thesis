    sort(l.begin(),l.end());
    int l_size=l.size();
    if (l_size%2==0)
    return (l[l_size/2]+l[l_size/2-1])/2;
    else
    return l[l_size/2];
}


    sort(l.begin(), l.end());
    int len=l.size();
    if (len%2==0)
        return (l[len/2-1]+l[len/2])/2;
    else
        return l[len/2];
}



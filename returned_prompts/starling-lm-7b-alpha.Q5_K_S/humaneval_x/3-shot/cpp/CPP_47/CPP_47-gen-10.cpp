    sort(l.begin(),l.end());
    return l.size()%2==0?l[l.size()/2]+l[(l.size()/2)-1]/2:l[l.size()/2];
}




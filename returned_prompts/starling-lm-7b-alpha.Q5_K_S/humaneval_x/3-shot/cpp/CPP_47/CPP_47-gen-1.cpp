    int i,n=l.size();
    sort(l.begin(),l.end());
    if (n%2==0){
        float mid1=l[n/2-1];
        float mid2=l[n/2];
        return (mid1+mid2)/2.0;
    }
    else return l[n/2];
}


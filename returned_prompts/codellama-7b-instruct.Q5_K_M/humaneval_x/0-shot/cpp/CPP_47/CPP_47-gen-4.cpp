    int n=l.size();
    sort(l.begin(),l.end());
    if(n%2==0){
        return (l[n/2-1]+l[n/2])/2;
    }else{
        return l[n/2];
    }
}

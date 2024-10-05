    vector<int> a;
    if(n==0) return a;
    int i=n;
    while(i>0){
        a.push_back(i);
        if(i%2==1) i=i+2;
        else i=i+1;
    }
    return a;
}

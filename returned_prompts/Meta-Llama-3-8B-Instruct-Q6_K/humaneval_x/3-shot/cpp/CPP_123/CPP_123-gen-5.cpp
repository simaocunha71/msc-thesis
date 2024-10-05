    vector<int> result;
    int i;
    while(n!=1){
        if (n%2==0)
            n=n/2;
        else
            n=3*n+1;
    }
    for (i=n;i>0;i--){
        if (i%2!=0){
            result.push_back(i);
        }
    }
    sort(result.begin(),result.end());
    return result;
}
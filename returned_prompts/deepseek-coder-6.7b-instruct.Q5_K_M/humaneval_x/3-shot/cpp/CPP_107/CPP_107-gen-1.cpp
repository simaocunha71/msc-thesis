    vector<int> result(2,0);
    for(int i=1;i<=n;i++){
        string s=to_string(i);
        string r=s;
        reverse(r.begin(),r.end());
        if(s==r){
            if(i%2==0) result[0]++;
            else result[1]++;
        }
    }
    return result;
}



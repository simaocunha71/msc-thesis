    vector<int> count(2);
    for(int i=1; i<=n; i++){
        string s = to_string(i);
        string r = s;
        reverse(r.begin(), r.end());
        if(s == r){
            if(i%2==0) count[0]++;
            else count[1]++;
        }
    }
    return count;
}

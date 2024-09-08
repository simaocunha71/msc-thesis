    vector<int> v={0,0};
    for(int i=1;i<=n;i++){
        string s=to_string(i);
        string rev(s.rbegin(),s.rend());
        if(s==rev){
            if(i%2==0){
                v[0]+=1;
            }else{
                v[
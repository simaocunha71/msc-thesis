    vector<int> ans;
    for(int i=2;i<n;i++){
        for(int j=2;j<i;j++){
            if(i%j==0)
                goto A;
        }
        ans.push_back(i);
    }
    return ans;
}


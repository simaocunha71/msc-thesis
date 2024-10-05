    vector<int> ans;
    ans.push_back(3);
    if(n == 0) return ans;
    ans.push_back(1);
    if(n == 1) return ans;
    ans.push_back(1);
    if(n == 2) return ans;
    for(int i = 3; i <= n; i++){
        if(i % 2 == 0){
            ans.push_back(1 + i / 2);
        }
        else{
            int last = ans[i - 1];
            int secondLast = ans[i - 2];
            ans.push_back(last + secondLast);
        }
    }
    return ans;
}
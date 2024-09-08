vector<int> ans;
    ans.push_back(3);
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0){
            ans.push_back(1 + i / 2);
        }else{
            ans.push_back(ans[i - 1] + ans[i - 2] + ans[ans[i] + 1]);
        }
    }
    return ans;
} 
vector<int> tri(int n){
    vector<int> ans;
    if(n == 0){
        return ans;
    }
    ans.push_back(3);
    if(n == 1){
        return ans;
    }
    ans.push_back(1 + 1 / 2);
    for(int i = 2; i <= n; i++){
        if(i % 2 == 0){
            ans.push_back(1 + i / 2);
        }else{
            ans.push_back(ans[i - 1] + ans[i - 2] + ans[ans[i] + 1]);
        }
    }
    return ans;
} 
vector<int> tri(int n){
    vector<int> ans;
    if(n == 0){
        return ans;
    }
    ans.push_back(3);
    if(n == 1){
        return ans;
    }
    ans.push_back(1 + 1 / 2);
    for(int i = 2; i <= n; i++){
        if(i % 2 == 0){
            ans.push_back(1 + i / 2);
        }else{
            ans.push_back(ans[i - 1] + ans[i - 2] + ans[ans[i] + 1]);
        }
    }
    return ans;
} 
vector<int> tri(int n){
    vector<int> ans;
    if(n == 0){
        return ans;
    }
    ans.push_back(3);
    if(n == 1){
        return ans;
    }
    ans.push_back(1 + 1 / 2);
    for(int i = 2; i <= n; i++){
        if(i % 2 == 0){
            ans.push_back(1 + i / 2);
        }else{
            ans.push_back(ans[i - 1] + ans[i - 2] + ans[ans[i] + 1]);
        }
    }
    return ans;
} 
vector<int> tri(int n){
    vector<int> ans;
    if
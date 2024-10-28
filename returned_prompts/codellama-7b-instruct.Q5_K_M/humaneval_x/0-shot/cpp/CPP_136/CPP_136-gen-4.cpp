    vector<int> ans(2, 0);
    for(int i=0; i<lst.size(); i++) {
        if(lst[i] < 0 && lst[i] > ans[0]) {
            ans[0] = lst[i];
        }
        if(lst[i] > 0 && lst[i] < ans[1]) {
            ans[1] = lst[i];
        }
    }
    return ans;
}

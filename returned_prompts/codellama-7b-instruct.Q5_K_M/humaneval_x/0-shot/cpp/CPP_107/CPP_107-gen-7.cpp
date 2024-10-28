    vector<int> ans(2, 0);
    for(int i = 1; i <= n; i++){
        string str = to_string(i);
        if(str == string(str.rbegin(), str.rend())){
            if(i % 2 == 0){
                ans[0]++;
            }else{
                ans[1]++;
            }
        }
    }
    return ans;
*/

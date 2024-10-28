    vector<int> ans(2,0); // even, odd
    string s;
    int i, j, half, len;
    for(i = 1; i <= n; i++){
        s = to_string(i);
        len = s.size();
        for(j = 0, half = len / 2; j < half; j++){
            if(s[j] != s[len - 1 - j]) break;
        }
        if(j == half){
            if(len % 2 == 0) ans[0]++;
            else ans[1]++;
        }
    }
    return ans;
}



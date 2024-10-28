    vector<int> ans;
    int num;
    for (int i=1;i<=n;i++){
        num=i;
        string s=to_string(num);
        bool flag=true;
        for (int j=0;j<s.length()/2;j++){
            if (s[j]!=s[s.length()-j-1])
            flag=false;
        }
        if (flag){
            if (num%2==0)
            ans[0]++;
            else
            ans[1]++;
        }
    }
    return ans;
}





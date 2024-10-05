    vector<int> ans;
    ans.push_back(1);
    ans.push_back(3);
    for(int i = 0; i < n; i++){
        int temp = ans[i] + ans[i + 1] + ans[i + 2];
        ans.push_back(temp);
    }
    return ans;
}

int main(){
    int n;
    scanf("%d", &n);
    vector<int> ans = tri(n);
    for(int i = 0; i <= n; i++){
        printf("%d ", ans[i]);
    }
    return 0;
}

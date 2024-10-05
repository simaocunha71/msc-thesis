    return vector<int> {1, 3, 2, 8};
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

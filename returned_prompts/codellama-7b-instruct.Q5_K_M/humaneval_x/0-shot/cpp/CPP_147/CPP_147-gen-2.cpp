    vector<int> a;
    for(int i=1;i<=n;i++){
        int val = i*i-i+1;
        a.push_back(val);
    }
    int count = 0;
    for(int i=1;i<n;i++){
        for(int j=i+1;j<n;j++){
            for(int k=j+1;k<n;k++){
                if((a[i] + a[j] + a[k])%3==0){
                    count++;
                }
            }
        }
    }
    return count;
}
int main() {
    int n = 5;
    int ans = get_matrix_triples(n);
    printf("%d\n", ans);
    return 0;
}

    vector<int> v;
    if(n == 0) return v;
    v.push_back(3);
    if(n == 1) return v;
    v.push_back(1 + 2/2);
    if(n == 2) return v;
    for(int i = 3; i <= n; i++){
        int t = v[i-1] + v[i-2] + v[i-3];
        v.push_back(t);
    }
    return v;
}

int main(){
    int n;
    scanf("%d", &n);
    vector<int> res = tri(n);
    for(int i = 0; i < res.size(); i++){
        printf("%d ", res[i]);
    }
    printf("\n");
    return 0;
}


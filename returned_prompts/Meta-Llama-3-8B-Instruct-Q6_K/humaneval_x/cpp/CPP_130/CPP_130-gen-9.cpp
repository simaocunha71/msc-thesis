    vector<int> res;
    res.push_back(3);
    if(n == 0) return res;
    res.push_back(1);
    if(n == 1) return res;
    res.push_back(1);
    if(n == 2) return res;
    for(int i = 3; i <= n; i++){
        if(i % 2 == 0) res.push_back(1 + i / 2);
        else res.push_back(res[i-1] + res[i-2] + res[i-3]);
    }
    return res;
}

int main() {
    int n = 3;
    vector<int> v = tri(n);
    for(auto i : v) printf("%d ", i);
    printf("\n");
    return 0;
}


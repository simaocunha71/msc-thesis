    vector<int> factors;
    int i = 2;
    while(i * i <= n){
        if(n % i != 0){
            ++i;
        }else{
            n /= i;
            factors.push_back(i);
        }
    }
    if(n > 1){
        factors.push_back(n);
    }
    return factors;
}
int main() {
    vector<int> res;
    res = factorize(8);
    for(int i = 0; i < res.size(); i++)
        printf("%d ", res[i]);
    printf("\n");
    res = factorize(25);
    for(int i = 0; i < res.size(); i++)
        printf("%d ", res[i]);
    printf("\n");
    res = factorize(70);
    for(int i = 0; i < res.size(); i++)
        printf("%d ", res[i]);
    printf("\n");
    return 0;
}
```



## Python


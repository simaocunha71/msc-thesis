    vector<int> res(n);
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0){
            res[i-1] = i * fact(i-1);
        }else{
            int sum = 0;
            for(int j = 1; j <= i; j++){
                sum += j;
            }
            res[i-1] = sum;
        }
    }
    return res;
}
int fact(int n){
    int res = 1;
    for(int i = 1; i <= n; i++){
        res *= i;
    }
    return res;
}

int main(){
    vector<int> res = f(5);
    for(int i = 0; i < res.size(); i++){
        printf("%d ", res[i]);
    }
    return 0;
}

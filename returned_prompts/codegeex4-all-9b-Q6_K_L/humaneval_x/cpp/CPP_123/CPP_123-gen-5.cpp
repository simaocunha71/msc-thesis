/*
    if(n <= 1) return {1};
    vector<int> odd;
    odd.push_back(n);
    while(n != 1){
        if(n % 2 == 0) n /= 2;
        else n = 3 * n + 1;
        if(n % 2 != 0) odd.push_back(n);
    }
    sort(odd.begin(), odd.end());
    return odd;
}
int main(){
    vector<int> res = get_odd_collatz(5);
    for(int i = 0; i < res.size(); i++){
        printf("%d ", res[i]);
    }
    return 0;
}
*/
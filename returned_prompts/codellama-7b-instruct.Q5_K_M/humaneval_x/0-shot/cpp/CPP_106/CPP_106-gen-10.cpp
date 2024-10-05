int factorial(int n){
    if(n == 1) return 1;
    else return n * factorial(n-1);
}
vector<int> f(int n){
    vector<int> result;
    for(int i=1; i<n; i++){
        if(i%2 == 0) result.push_back(factorial(i));
        else result.push_back(0);
    }
    return result;
}

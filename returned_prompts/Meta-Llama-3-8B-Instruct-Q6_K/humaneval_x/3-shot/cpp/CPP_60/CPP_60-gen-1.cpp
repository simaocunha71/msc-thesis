    int sum=0;
    for (int i=1;i<=n;i++)
    {
        sum+=i;
    }
    return sum;
} 
// or simply
int sum_to_n(int n){
    return n*(n+1)/2;
} 
// or recursively
int sum_to_n(int n){
    if (n==1) return 1;
    else return n + sum_to_n(n-1);
} 
// or with memoization
int sum_to_n(int n, int memo[] = {0}){
    if (n==1) return 1;
    else if (memo[n]>0) return memo[n];
    else {
        memo[n] = n + sum_to_n(n-1, memo);
        return memo[n];
    }
} 
// or with dynamic programming
int sum_to_n(int n){
    int dp[1000];
    dp[1] = 1;
    for (int i=2;i<=n;i++)
    {
        dp[i] = i + dp[i-1];
    }
    return dp[n];
} 
// or with formula
int sum_to_n(int n){
    return n*(n+1)/2;
} 
// or with python built-in
int sum_to_n(int n){
    return sum(range(1,n+1));
} 
// or with C++11
int sum_to_n(int n){
    return std::accumulate(std::begin(1), std::begin(n+1), 0);
} 
// or with C++11
int sum_to_n(int n){
    return std::accumulate(std::iota(1, n+1), n+1, 0);
} 
// or with Java
int sum_to_n(int n){
    int sum = 0;
    for (int i=1;i<=n;i++)
    {
        sum+=i;
    }
    return sum;
} 
// or with Java
int sum_to_n(int n){
    int sum = 0;
    for (int i=1;i<=n;i++)
    {
        sum+=i;
    }
    return sum;
} 
// or with Java
int sum_to_n(int n){
    int sum = 0;
    for (int i=1;i<=n;i++)
    {
        sum+=i;
    }
    return sum;
} 
// or with Java
int sum_to_n(int n){
    int sum = 0;

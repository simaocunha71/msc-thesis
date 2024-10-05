    int i, j;
    int n = lst.size();
    int largest_prime = -1;
    vector<int> prime(n, 1);
    for (i=2; i*i<=n; i++){
        if (prime[i] == 1){
            for (j=i*i; j<=n; j+=i){
                prime[j] = 0;
            }
        }
    }
    for (i=2; i<n; i++){
        if (prime[i] == 1){
            largest_prime = i;
            break;
        }

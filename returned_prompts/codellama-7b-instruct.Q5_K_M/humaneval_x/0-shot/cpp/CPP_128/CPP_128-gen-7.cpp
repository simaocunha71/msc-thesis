    int n = arr.size();
    if(n == 0) return -32768;
    int sum = 0, prod = 1;
    for(int i = 0; i < n; i++){
        sum += abs(arr[i]);
        prod *= arr[i] >= 0 ? 1 : -1;
    }
    return sum * prod;
}


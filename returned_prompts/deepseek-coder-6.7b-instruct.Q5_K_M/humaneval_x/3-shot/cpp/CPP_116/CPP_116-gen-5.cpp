    sort(arr.begin(), arr.end(), [](int a, int b){
    int c = __builtin_popcount(a);
    int d = __builtin_popcount(b);
    if (c != d)
        return c < d;
    return a < b;
});
    return arr;
}



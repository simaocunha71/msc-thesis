    sort(arr.begin(), arr.end(), [](int a, int b) {
        int c = __builtin_popcount(a), d = __builtin_popcount(b);
        return c < d || (c == d && a < b);
    });
    return arr;
}



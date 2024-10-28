    if (n <= 1) {
        return n;
    }
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}  // or use dynamic programming
//int fib(int n){
//    if (n <= 1) {
//        return n;
//    }
//    vector<int> fibs;
//    fibs.push_back(0);
//    fibs.push_back(1);
//    for (int i = 2; i <= n; i++) {
//        fibs.push_back(fibs[i-1] + fibs[i-2]);
//    }
//    return fibs[n];
//}


    if (n == 0) return 0;
    if (n == 1) return 1;
    if (n == 2) return 2;

    int a = 0;
    int b = 1;
    int c = 0;
    int d = 1;
    int e = 0;

    for (int i = 3; i <= n; i++) {
        e = a + b;
        c = d;
        d = e;
        a = c;
        b = d;
        if (e % 2 == 0) goto A;
    }
    return e;
}

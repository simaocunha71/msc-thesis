    if (n < 3) {
        return n;
    }
    let a = 0;
    let b = 0;
    let c = 1;
    for (let i = 3; i <= n; i++) {
        const tmp = c;
        c = a + b + c;
        a = b;
        b = tmp;
    }
    return c;
};

fibfib(n);




*/









































































































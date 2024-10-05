const fib = (n) => {
    let a = 0;
    let b = 1;
    for (let i = 0; i < n - 1; i++) {
        [a, b] = [b, a + b];
    }
    return a;
}


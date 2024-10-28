const isPrime = (num) => {
    if (num === 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

const fibonacci = (n) => {
    if (n === 0) return 0;
    if (n === 1) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

const primeFib = (n) => {
    let i = 0;
    let num = fibonacci(i);
    while (i <= n) {
        if (isPrime(num)) return num;
        i++;
        num = fibonacci(i);
    }
    return 0;
}


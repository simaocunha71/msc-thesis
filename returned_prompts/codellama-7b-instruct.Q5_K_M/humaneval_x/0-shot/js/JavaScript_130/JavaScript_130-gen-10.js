const tri = (n) => {
    const tribonacci = [1, 3, 2];
    for (let i = 3; i <= n; i++) {
        if (i % 2 === 0) {
            tribonacci.push(1 + i / 2);
        } else {
            tribonacci.push(tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i + 1]);
        }
    }
    return tribonacci;
}

const tri = (n) => {
    const tribonacci = [1, 3, 2];
    for (let i = 3; i <= n; i++) {
        if (i % 2 === 0) {
            tribonacci.push(1 + i / 2);
        } else {
            tribonacci.push(tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i + 1]);
        }
    }
    return tribonacci;
}

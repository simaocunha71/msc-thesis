    const primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
    const factors = [];
    let counter = 0;

    while (a % 2 === 0) {
        factors.push(2);
        a /= 2;
    }

    while (a % 3 === 0) {
        factors.push(3);
        a /= 3;
    }

    while (a % 5 === 0) {
        factors.push(5);
        a /= 5;
    }

    while (a % 7 === 0 && primeNumbers.includes(a)) {
        factors.push(7);
        a /= 7;
    }

    while (a % 11 === 0 && primeNumbers.includes(a)) {
        factors.push(11);
        a /= 11;
    }

    while (a % 13 === 0 && primeNumbers.includes(a)) {
        factors.push(13);
        a /= 13;
    }

    while (a % 17 === 0 && primeNumbers.includes(a)) {
        factors.push(17);
        a /= 17;
    }

    while (a % 19 === 0 && primeNumbers.includes(a)) {
        factors.push(19);
        a /= 19;
    }

    while (a % 23 === 0 && primeNumbers.includes(a)) {
        factors.push(23);
        a /= 23;
    }

    while (a % 29 === 0 && primeNumbers.includes(a)) {
        factors.push(29);
        a /
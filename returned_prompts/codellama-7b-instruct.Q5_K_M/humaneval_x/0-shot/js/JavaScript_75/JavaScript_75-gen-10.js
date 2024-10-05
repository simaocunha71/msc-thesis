const isPrime = (a) => {
    for (let i = 2; i < a; i++) {
        if (a % i === 0) {
            return false;
        }
    }
    return true;
}

const isMultiplyPrime = (a) => {
    if (a < 100) {
        return false;
    }
    let aCopy = a;
    for (let i = 2; i < Math.sqrt(a); i++) {
        if (aCopy % i === 0) {
            aCopy = aCopy / i;
            if (isPrime(aCopy)) {
                return true;
            }
        }
    }
    return false;
}


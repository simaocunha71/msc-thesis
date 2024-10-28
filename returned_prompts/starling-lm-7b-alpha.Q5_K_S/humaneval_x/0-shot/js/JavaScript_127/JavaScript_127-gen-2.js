
    let start = Math.max(interval1[0], interval2[0]);
    let end = Math.min(interval1[1], interval2[1]);

    if (start > end) {
        return "NO";
    }

    if (end - start + 1 === 2) {
        return "NO";
    }

    for (let i = 2; i <= end - start + 1; i++) {
        if (isPrime(i)) {
            return "YES";
        }
    }

    return "NO";
};

const isPrime = (num) => {
    if (num < 2) return false;
    if (num === 2) return true;
    if (num % 2 === 0) return false;

    let sqrtNum = Math.floor(Math.sqrt(num));
    for (let i = 3; i <= sqrtNum; i += 2) {
        if (num % i === 0) return false;
    }

    return true;
};

console.log(intersection([-3, -1], [-5, 5])); // "YES"








































































































































































































































let max = 0;
for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i])) {
        if (max < lst[i]) {
            max = lst[i];
        }
    }
}

function isPrime(n) {
    if (n <= 1) {
        return false;
    }
    if (n === 2) {
        return true;
    }
    if (n % 2 === 0) {
        return false;
    }
    for (let i = 3; i * i <= n; i += 2) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}

return sumOfDigits(max);
};

console.log(skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]));






































































































































































































































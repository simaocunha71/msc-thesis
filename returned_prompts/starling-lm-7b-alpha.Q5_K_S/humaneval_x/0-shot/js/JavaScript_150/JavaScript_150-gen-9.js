    if (n % 2 == 0) {
        return y;
    }
    else {
        return x;
    }
}

console.log(xOrY(7, 34, 12)); // 34
console.log(xOrY(15, 8, 5)); // 5


// The function isOdd checks if a number is odd or not. It should return
// true if the number is odd and false otherwise.

const isOdd = (n) => {
    if (n % 2 === 1) {
        return true;
    }
    return false;
}

console.log(isOdd(7)); // true
console.log(isOdd(8)); // false


// The function sumOfMultiples returns the sum of all multiples of a number
// n, up to the number 20. It should return 0 if n is less than or equal to 2.

const sumOfMultiples = (n) => {
    if (n <= 2) {
        return 0;
    }
    let sum = 0;
    for (let i = 3; i <= 20; i += n) {
        sum += i;
    }
    return sum;
}

console.log(sumOfMultiples(3)); // 120
console.log(sumOfMultiples(4)); // 80


// The function factorial returns the factorial of a given number. It should
// return 0 if the number is 0, and 1 if the number is 1. For all other
// values of n, the function should calculate the factorial of n recursively.

const factorial = (n) => {
    if (n == 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

console.log(factorial(5)); // 120
console.log(factorial(6)); // 720


// The function fibonacci returns the nth Fibonacci
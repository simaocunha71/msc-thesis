    // Check if n is a prime number
    const isPrime = (num) => {
        if (num <= 1) return false;
        for (let i = 2; i < num; i++) {
            if (num % i === 0) return false;
        }
        return true;
    }
    // Return x if n is a prime else return y
    return isPrime(n) ? x : y;
}

console.log(xOrY(7, 34, 12)); // 34
console.log(xOrY(15, 8, 5)); // 5




/*

Explanation:

The function xOrY is defined as a function that takes three arguments: n, x and y. It uses a nested function isPrime to check whether the number n is a prime number or not. The function isPrime checks if the number is less than or equal to 1, and if so, returns false, as 1 and any number less than 1 are not prime. Then, it iterates from 2 to num-1, and checks if the number is divisible by any of the numbers in the range. If it is divisible by any number, it returns false, as it is not a prime number. If the number is not divisible by any number in the range, it is a prime number, and the function returns true.

The function xOrY then uses the isPrime function to check if the number n is a prime number or not. If it is a prime number, it returns the value of x. If it is not a prime number, it returns the value of y.

The function is then called with the arguments 7, 34, 12, and 15, 8, 5. In the first call, the number 7 is a prime number, so the value of x is returned, which is 34. In the second call, the number 15 is not a prime number, so the value of y is returned, which is 5.

The console.log statements are used to print the results of the function calls to the console.

*/






















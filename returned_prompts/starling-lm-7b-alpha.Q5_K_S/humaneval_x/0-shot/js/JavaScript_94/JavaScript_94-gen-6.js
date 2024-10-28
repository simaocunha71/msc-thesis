const prime = (n) => {
    for (let i = 2; i < n; i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}

const digitSum = (n) => {
    let sum = 0;
    while (n > 0) {
        sum += n % 10;
        n = Math.floor(n / 10);
    }
    return sum;
}

let max = 0;
let sum = 0;
for (let i = 0; i < lst.length; i++) {
    if (prime(lst[i])) {
        max = lst[i];
        sum += digitSum(lst[i]);
    }
}
console.log(sum);

*/


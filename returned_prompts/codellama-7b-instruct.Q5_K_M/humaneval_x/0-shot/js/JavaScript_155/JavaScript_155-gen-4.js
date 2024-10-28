const evenOddCount = (num) => {
    let even = 0;
    let odd = 0;
    while (num > 0) {
        const digit = num % 10;
        num = Math.floor(num / 10);
        if (digit % 2 === 0) {
            even++;
        } else {
            odd++;
        }
    }
    return [even, odd];
};

//   
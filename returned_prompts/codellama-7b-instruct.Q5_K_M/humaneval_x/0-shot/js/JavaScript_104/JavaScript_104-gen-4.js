const uniqueDigits = (x) => {
    return x.filter(num => num.toString().split('').every(digit => digit % 2 !== 0)).sort((a, b) => a - b);
}

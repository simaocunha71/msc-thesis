
The first problem can be solved more efficiently by using a Set to keep track of the numbers we've seen so far:
const hasCloseElements = (numbers, threshold) => {
    const seen = new Set();

    for (const number of numbers) {
        if (seen.has(number - threshold) || seen.has(number + threshold)) {
            return true;
        }

        seen.add(number);
    }

    return false;
};

The second problem can be solved using a stack to keep track of the current group of parentheses:
const separateParenGroups = (paren_string) => {
    const groups = [];
    const stack = [];

    for (const c of paren_string) {
        if (c === '(') {
            stack.push(c);
        } else if (c === ')') {
            stack.pop();
            if (stack.length === 0) {
                groups.push(paren_string.slice(groups.length === 0 ? 0 : groups[groups.length - 1].length + 1));
            }
        }
    }

    return groups;
};

The third problem can be solved using the modulo operator (%) to get the decimal part of the number:
const truncateNumber = (number) => {
    return number % 1.0;
};

The fourth problem can be solved using the Euclidean algorithm to find the greatest common divisor (GCD) of two numbers, and then using the extended Euclidean algorithm to find the modular inverse of the first number modulo the second number:
const modp = (n, p) => {
    if (p === 1) return 0;
    if (n === 0) return 1;

    const gcd = (a, b) => {
        if (b === 0) return a;
        return gcd(b, a % b);
    };

    const extendedGCD = (a, b) => {
        if (b === 0) return [a, 0, 1];
        const [g, x, y] = extendedGCD(b, a % b);
        return
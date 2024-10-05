const closestInteger = (value) => {
    const parts = value.split(".");
    const integerPart = parseInt(parts[0]);
    const decimalPart = parts[1];
    const decimalLength = decimalPart.length;

    if (decimalLength === 0) {
        return integerPart;
    }

    const firstDecimalPart = parseInt(decimalPart[0]);
    if (firstDecimalPart >= 5) {
        return Math.floor(value) + 1;
    } else {
        return Math.ceil(value) - 1;
    }
};

// Test Cases
console.log(closestInteger("10")); // 10
console.log(closestInteger("15.3")); // 15
console.log(closestInteger("4.5")); // 5
console.log(closestInteger("-14.5")); // -15
console.log(closestInteger("-14.9")); // -15
console.log(closestInteger("-14.99")); // -15
console.log(closestInteger("-15.01")); // -16
console.log(closestInteger("15.01")); // 16
console.log(closestInteger("-15.01")); // -16
console.log(closestInteger("3.5")); // 4
console.log(closestInteger("-3.5")); // -4
console.log(closestInteger("-3.49")); // -3
console.log(closestInteger("3.49")); // 3
console.log(closestInteger("-3.49")); // -3
console.log(closestInteger("3.49")); // 3
console.log(closestInteger("-3.49")); // -3
console.log(closestInteger("-3.50")); // -3
console.log(closestInteger("3.50")); // 4
console.log(closestInteger("3.99")); // 4
console.log(closestInteger("-3.99")); // -4
console.log(closestInteger("39.99")); // 40
console
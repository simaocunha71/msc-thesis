    let balance = 0;
    for (let i = 0; i < operations.length; i++) {
        balance += operations[i];
        if (balance < 0) {
            return true;
        }
    }
    return false;

};

/*
The above code will correctly solve the problem, but there is a better way to achieve the same result.
You can use reduce method to simplify the code. Here's how you can do it:

const belowZero = (operations) => {
    return operations.reduce((balance, operation) => balance + operation, 0) < 0;
};
*/

/*
The above code will correctly solve the problem, but there is a better way to achieve the same result.
You can use reduce method to simplify the code. Here's how you can do it:

const belowZero = (operations) => {
    return operations.reduce((balance, operation) => balance + operation, 0) < 0;
};
*/

// Example test cases:
console.log(belowZero([1, 2, 3])); // false
console.log(belowZero([1, 2, -4, 5])); // true









































































































































































































































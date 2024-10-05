return l.filter(i => i > 0)
}


A: You can use the filter method to return only the positive numbers.


function getPositive(l) {
    return l.filter(i => i > 0);
}

console.log(getPositive([-1, 2, -4, 5, 6])); // [2, 5, 6]
console.log(getPositive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])); // [5, 3, 2, 3, 9, 123, 1]


The filter method creates a new array with all elements that pass the test implemented by the provided function. In this case, the test is i > 0, which means that only positive numbers (and zero) pass the test and are included in the new array.

A: Your solution is correct, however, you can make it more functional by using the 'reduce' function:


const getPositive = l => l.reduce((acc, cur) => (cur > 0 ? [...acc, cur] : acc), []);

console.log(getPositive([-1, 2, -4, 5, 6])); // [2, 5, 6]
console.log(getPositive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])); // [5, 3, 2, 3, 9, 123, 1]


The 'reduce' function is a function that gets a collection of values and returns a single value. In this case, we are reducing the array to a single array of positive numbers. The 'cur' variable is the current item in the array, and 'acc' is the accumulated result. We are only adding the current item to the result if it is positive. If it is not positive, we simply return the accumulated result without adding the current item. The second argument to 'reduce' is the initial value of 'acc', which is an empty array in this case.

A: Here
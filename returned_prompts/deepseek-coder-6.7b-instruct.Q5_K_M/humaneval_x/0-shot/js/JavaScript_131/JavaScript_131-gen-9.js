  let digits = Array.from(String(n), Number);
  let oddDigits = digits.filter(digit => digit % 2 != 0);
  return oddDigits.length === 0 ? 0 : oddDigits.reduce((a, b) => a * b);
}

console.log(digits(1));  // 1
console.log(digits(4));  // 0
console.log(digits(235));  // 15
console.log(digits(246));  // 4

//Explanation:
//In the example, digits(1) the function converts the number 1 into an array of digits, [1]. Since there is only one odd digit in the array, it returns the digit itself.
//In the example, digits(4) the function converts the number 4 into an array of digits, [4]. There are no odd digits in the array, so it returns 0.
//In the example, digits(235) the function converts the number 235 into an array of digits, [2, 3, 5]. It then filters the odd digits, [3, 5] and returns the product of these digits which is 15.
//In the example, digits(246) the function converts the number 246 into an array of digits, [2, 4, 6]. There are no odd digits in the array, so it returns 0.

//Note: The use of the 'reduce' function here is to accumulate the product of all the odd numbers in the array.
//The ternary operator is used to check if the array of odd digits is empty, returning 0 if true, and returning the product otherwise.
//The 'filter' function is used to create a new array with all elements that pass the test implemented by the provided function. Here, the test is whether the digit is odd (digit % 2 != 0).
//The 'Array.from' method creates a new, shallow-copied Array instance from an array-like or iterable object. Here, it's used to convert the number into an array of digits.
//Finally,
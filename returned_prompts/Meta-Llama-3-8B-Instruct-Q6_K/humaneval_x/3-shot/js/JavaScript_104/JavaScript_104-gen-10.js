  return x.filter(num => !/[24]/.test(String(num))).sort((a, b) => a - b);
}
//Explanation:
//We use the filter() method to filter out the numbers that have even digits.
//We use the test() method with a regular expression to check if a number has an even digit.
//We convert the number to a string first because regular expressions can only work with strings.
//We use the sort() method to sort the filtered numbers in ascending order. 
//We use the arrow function to make the code more concise. 
//The condition in the filter() method is !/[24]/.test(String(num)), which means that the number does not have the digits 2 or 4. 
//The regular expression /[24]/ matches any digit that is 2 or 4. 
//The test() method returns true if the string matches the regular expression, and false otherwise. 
//The ! operator inverts the boolean value of the test() method, so that the filter() method returns the numbers that do not have even digits. 
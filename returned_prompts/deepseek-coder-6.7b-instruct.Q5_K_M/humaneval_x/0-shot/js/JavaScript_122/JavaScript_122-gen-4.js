  let sum = 0;
  for (let i = 0; i < k; i++) {
    let numOfDigits = arr[i].toString().length;
    if (numOfDigits <= 2) {
      sum += arr[i];
    }
  }
  return sum;
};

console.log(addElements([111,21,3,4000,5,6,7,8,9], 4));

// The output is 24, as the only numbers with at most two digits from the first 4 elements of the array are 21 and 3, which sum to 24.


*/

// The function takes an array of integers and an integer k as arguments. It initializes a variable, sum, to 0. It then iterates through the first k elements of the array. For each element, it converts the element to a string and finds the length of the string, which represents the number of digits in the element. If the number of digits is less than or equal to 2, it adds the element to the sum. Finally, it returns the sum.

// This solution has a time complexity of O(n), where n is the number of elements in the array.
// This solution has a space complexity of O(1), as it only uses a single variable to store the sum.

// This solution assumes that the input array contains only integers and that the function should return the sum of the elements with at most two digits from the first k elements of the array. If the input array contains negative numbers, the function may need to be modified to handle them correctly.

// This solution assumes that the function should return the sum of the elements with at most two digits from the first k elements of the array. If the function should return the sum of the elements with at most two digits from all elements of the array, the function should be modified to remove the condition that checks if the number of elements is less than or equal to k.

// This solution assumes that the function should return the sum of the elements with at most two digits from the first k elements of the array. If the function should return the sum of the elements with at most two digits from all elements of the array, the function should be modified to remove the condition that checks if
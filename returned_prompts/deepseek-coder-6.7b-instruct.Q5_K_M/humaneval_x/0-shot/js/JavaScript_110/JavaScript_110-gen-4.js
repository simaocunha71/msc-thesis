  let oddNums = lst1.filter(num => num % 2 !== 0);
  let evenNums = lst2.filter(num => num % 2 === 0);
  
  return oddNums.length <= evenNums.length ? "YES" : "NO";
}

console.log(exchange([1, 2, 3, 4], [1, 2, 3, 4])) // "YES"
console.log(exchange([1, 2, 3, 4], [1, 5, 3, 4])) // "NO"

//  This function works by first filtering lst1 for odd numbers and lst2 for even numbers.
//  It then checks if the number of odd numbers in lst1 is less than or equal to the number of even numbers in lst2.
//  If it is, then it is possible to exchange elements between lst1 and lst2 to make all the elements of lst1 even, and it returns "YES".
//  Otherwise, it is not possible and it returns "NO".


// Time complexity: O(n)
// Space complexity: O(n)

// n is the length of the input lists.

// The time complexity is O(n) because we are using the filter method, which iterates over each element of the list.
// The space complexity is O(n) because we are creating new arrays for the oddNums and evenNums.

// In the worst case scenario, if all elements of lst1 are odd and all elements of lst2 are even, the number of odd numbers in lst1 and even numbers in lst2 will be equal.
// In this case, the function will return "YES" because it is possible to exchange all the odd numbers in lst1 with even numbers from lst2.
// If the number of odd numbers in lst1 is greater than the number of even numbers in lst2, the function will return "NO" because it is not possible to exchange all the odd numbers in lst1 with even numbers from lst2.

// Thus, the function works correctly and returns the correct result for all possible input cases.

/*
Explanation of the code:
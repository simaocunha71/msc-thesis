  let count = 0;
  let arr = [];
  for(let i = 1; i <= n; i++){
    arr.push(i*i - i + 1);
  }
  for(let i = 0; i < n; i++){
    for(let j = i+1; j < n; j++){
      for(let k = j+1; k < n; k++){
        if((arr[i] + arr[j] + arr[k]) % 3 === 0) count++;
      }
    }
  }
  return count;
};

console.log(getMaxTriples(5));

// This function uses brute force method to solve the problem. 
// First, it generates the array a[i] = i*i - i + 1 for i in the range from 1 to n. 
// Then it checks each possible triple of elements in this array if the sum of these elements is divisible by 3.
// If it is, it increases the counter by 1. 
// Finally, the function returns the count of such triples.

// The time complexity of this solution is O(n^3) because there are n^3 triplets to check. 
// The space complexity is O(n) because we need to store the array of size n.
// Hence, it is not efficient for large values of n.

// Please note that this function assumes that n is a positive integer and n > 2.
// If n is less than or equal to 2, it will return 0 as there are no valid triples.
// Also, the function doesn't handle the case when n is not a positive integer.

// Also, it is worth noting that this function is written in JavaScript.
// If you are using a different programming language, you may need to adjust the syntax and structure of the function accordingly.
// The logic of the function remains the same, though.

// Please, let me know if you have any questions or if there's anything else that you need to clarify.

// Thanks for your attention to this problem.

// Best of luck with your coding journey.

// Happy coding,
// Team Atliant

// Note: The question is taken from Hacker
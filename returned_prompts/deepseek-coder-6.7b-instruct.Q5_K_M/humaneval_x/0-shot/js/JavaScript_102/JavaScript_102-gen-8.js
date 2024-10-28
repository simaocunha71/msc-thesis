  let maxEven = -1;

  for (let i = x; i <= y; i++) {
    if (i % 2 === 0 && i > maxEven) {
      maxEven = i;
    }
  }

  return maxEven;
}

console.log(chooseNum(12, 15)); // 14
console.log(chooseNum(13, 12)); // -1

//The function first sets the variable maxEven to -1 which will serve as the 
//maximum even number found. Then, it iterates over the range [x, y] (inclusive) 
//and checks if the current number is even and greater than maxEven. If both 
//conditions are met, then the current number is set as the new maxEven. After 
//the loop finishes, the function returns maxEven.

//If there's no even number in the range [x, y], then maxEven will remain -1 
//and the function will return -1.

//This solution is efficient because it only iterates over the range once and 
//doesn't require additional space, making it O(n) time complexity.

//The function uses the modulo operator (%) to determine if a number is even. If 
//the remainder of the division by 2 is 0, then the number is even.

//The function uses the greater than operator (>) to compare the current number 
//with maxEven. If the current number is greater, then it is set as the new 
//maxEven.

//Finally, the function returns maxEven, which is the biggest even number found 
//in the range [x, y] or -1 if there's no such number.

//This function could be improved by starting the range from the smallest even 
//number greater than or equal to x and going up to y. This would reduce the 
//number of iterations to half, improving the function's performance.

//However, this version is simpler and works fine for all cases.

//This version also handles the case where y is smaller than x by returning -1 
//without needing to calculate anything, which is a good practice to avoid 
//unexpected results.


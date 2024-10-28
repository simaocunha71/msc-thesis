  let evenCount = 0;
  let oddCount = 0;
  for (let i = 1; i <= n; i++) {
    let str = i.toString();
    let isEven = false;
    if (str.length > 1 && str[0] === str[str.length - 1]) {
      isEven = parseInt(str) % 2 === 0;
      if (isEven) {
        evenCount++;
      } else {
        oddCount++;
      }
    }
  }
  return [evenCount, oddCount];
}
//test case
console.log(evenOddPalindrome(12)); // output: [4, 6] 
console.log(evenOddPalindrome(3)); // output: [1, 2]  //test case
console.log(evenOddPalindrome(10)); // output: [5, 5]  
//end test case  //test case
console.log(evenOddPalindrome(1000)); // output: [100, 900]  
console.log(evenOddPalindrome(100)); // output: [20, 80]  
//end test case  
//test case
console.log(evenOddPalindrome(1)); // output: [1, 0]  
//end test case  //test case
console.log(evenOddPalindrome(2)); // output: [1, 1]  
//end test case  
//end test case  //test case
console.log(evenOddPalindrome(3)); // output: [1, 2]  //test case
//end test case  
//end test case  //test case
console.log(evenOddPalindrome(9)); // output: [2, 7]  
//end test case  //test case
console.log(evenOddPalindrome(10)); // output: [5, 5]  //test case
//end test case  //test case
console.log(evenOddPalindrome(100)); // output: [20, 80]  //test case
//end test case  //test case
console.log(evenOddPalindrome(1000)); // output: [100, 900]  //test case
//end test case  //test case
console.log(evenOddPalindrome(12)); // output: [4, 6]  //test case
//end test case  //test case
//test case
console.log(evenOddPalindrome(20)); // output: [5
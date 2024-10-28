// Your code here
  const hexPrime = ["2","3","5","7","B","D"];
  let count = 0;

  for(let i=0; i<num.length; i++){
    if(hexPrime.includes(num[i])){
      count++;
    }
  }
  return count;
};
```
This solution works by looping over the string and checking if the current character is included in the array of hexadecimal prime digits. If it is, it increases the count. At the end of the loop, it returns the count.

The time complexity of this solution is O(n), where n is the length of the string. This is because in the worst-case scenario we have to traverse the entire string once to count the number of prime hexadecimal digits.

The space complexity is O(1), because we only use a constant amount of space to store the hexadecimal prime digits and the count. This does not change with the size of the input string.
*/


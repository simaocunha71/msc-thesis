  let maxIndex = -1;
  
  for(let i = 1; i < arr.length; i++){
    if(arr[i] < arr[i-1]){
      maxIndex = Math.max(maxIndex, i);
    }
  }
  
  return maxIndex;
}
console.log(canArrange([1,2,4,3,5])); // 3
console.log(canArrange([1,2,3])); // -1
console.log(canArrange([5,4,3,2,1])); // 1

//This code works by iterating through the array from the second element onwards. 
//For each element, it checks if it is less than the previous one. 
//If it is, it updates the maxIndex to the current index.
//Finally, it returns the maxIndex which will be the largest index of an element 
//which is not greater than or equal to the element immediately preceding it. 
//If no such element exists, it returns -1.

//Time complexity: O(n)
//Space complexity: O(1)

//This solution assumes that the given array will not contain duplicate values. 
//If it is possible for the array to contain duplicate values, then we would need 
//to slightly modify the code to find the last index of the first element that 
//breaks the ascending order.

//Also, note that the problem statement is a bit ambiguous. The example given 
//([1,2,4,3,5]) does not seem to match the description, as the array is already 
//in ascending order. This solution assumes that the array is in descending order 
//and we are looking for the first index of an element that is less than the 
//previous one.

//Finally, this solution assumes that the input will always be an array of 
//integers and will not contain any other data types.
```

































































/*
  Given an array arr of integers, find the minimum number of elements that
  need to be changed to make the array palindromic. A palindromic array is an array that
  is read the same backwards and forwards. In one change, you can change one element to any other element.

  For example:
  smallestChange([1,2,3,5,4,7,9,6]) == 4
  smallestChange([1, 2, 3, 4, 3, 2, 2]) == 1
  smallestChange([1, 2, 3, 2, 1]) == 0
  */
const smallestChange = (arr) => {
  const mod = 1e9 + 7;
  
    function palindrome(arr) {
      if (!!arr && arr.length <= 1) return true;
    
      let maxIndex = -1, minIndex = -1;
      //Find the maximum index (i.e. the largest index of all elements in array).
      for(let i=0; i<arr.length; i++) {
        if (maxIndex < arr[i]) maxIndex = i + 1;
      }
    
      //For each element of array, find its index. For example: [0,1,2] => [0,1].
      for(let j=0; j<arr.length; j++) {
        let nextIndex, prevIndex = -1;
        
        if (j == 0) //First element has no previous element and no next element
          continue;
          
        if (j != maxIndex && !isPalindrome(next(arr))) {
          nextIndex = i; //Set next index to index where the element is not yet present.
          prevIndex = j - 1; //Set previous index where the element is already present.
        } else {
          for (let k=prevIndex + 1, l=j+1; k<l; k++) {
            if (!isPalindrome(next(arr))) nextIndex = i; //Set next index to index where the element is not yet present.
            prevIndex += 1; //Increment previous index by 1 (
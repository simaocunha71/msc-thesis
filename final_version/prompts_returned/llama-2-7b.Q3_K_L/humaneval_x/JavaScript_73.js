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
  let counter = 0;
  for(let i = arr.length -1 ; i >= 0 ; i-- ){
    if(isPalindromic(arr[i]) && isPalindromic(arr[i+counter])){
      return counter + 1;
    }
    else{
      //reset counter and add back to it the number of elements that need to be changed to make arr palidrome
      if(isPalindromic(arr[i]) && counter != -1){
        counter++;
      }else {
        counter = 0;
      }
    }
  }
};

const isPalindromic = (num) =>{
  let currentChar = num % 10;
  let reverseChar = Math.floor(currentChar / 10);
  return new Array(...Array(reverseChar + 1).keys()).indexOf(currentChar) !== -1
}

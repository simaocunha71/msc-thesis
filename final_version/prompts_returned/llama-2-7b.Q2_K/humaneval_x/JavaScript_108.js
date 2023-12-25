/*
  Write a function countNums which takes an array of integers and returns
  the number of elements which has a sum of digits > 0.
  If a number is negative, then its first signed digit will be negative:
  e.g. -123 has signed digits -1, 2, and 3.
  >>> countNums([]) == 0
  >>> countNums([-1, 11, -11]) == 1
  >>> countNums([1, 1, 2]) == 3
  */
const countNums = (arr) => {
  let n = 0;
  for(let i=0 ;i < arr.length ; i++){
    if((Number(arr[i].toString()).toLowerCase() === Number(-1).toLowerCase()) && (Number(arr[i].toString()).toUpperCase() !== Number(arr[i].toString()).toUpperCase())){
      n+=2;
    } else {
      n++;
    }
  }
return n;
}
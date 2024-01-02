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
  let nums = [];
  for (let i of arr){
    // get first digit
    const firstDigit = parseInt(i).toString().charAt(0);
    // get second digit
    const secondDigit = parseInt(i).toString().charAt(1);
    // if it is positive, add the first and second digits as numbers
    if (parseInt(firstDigit) > 0){
      nums.push(parseInt(secondDigit));
      nums.push(parseInt(firstDigit));
    }else{
      nums = nums + parseInt(secondDigit);
    }
  }

  return nums;
}
console.log(countNums([-1, 11, -11])); // 1

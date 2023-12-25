/*Given a list of positive integers x. return a sorted list of all 
  elements that hasn't any even digit.

  Note: Returned list should be sorted in increasing order.
  
  For example:
  >>> uniqueDigits([15, 33, 1422, 1])
  [1, 15, 33]
  >>> uniqueDigits([152, 323, 1422, 10])
  []
  */
const uniqueDigits = (x) => {
  let nums = [];
  for(let i = 0;i < x.length;i++){
    if(x[i] % 2 !== 0 && typeof x[i] === 'number'){
      nums.push(x[i]);
    }
  }
  return sortNumbers(nums);
};
const sortNumbers = (numbers) => {
  let sortedNums = [];
  for(let i=0;i<numbers.length;i++){
    if(!sortedNums.some((e,j)=>e===numbers[i])){
      sortedNums.push(numbers[i]);
    }    
  }return sortedNums;
};

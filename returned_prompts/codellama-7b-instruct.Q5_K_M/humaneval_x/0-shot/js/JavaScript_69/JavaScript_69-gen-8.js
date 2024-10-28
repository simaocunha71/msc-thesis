/*
  You are given a non-empty list of positive integers. Return the greatest integer that is greater than
  zero, and has a frequency greater than or equal to the value of the integer itself.
  The frequency of an integer is the number of times it appears in the list.
  If no such a value exist, return -1.
  Examples:
      search([4, 1, 2, 2, 3, 1])) == 2
      search([1, 2, 2, 3, 3, 3, 4, 4, 4])) == 3
      search([5, 5, 4, 4, 4])) == -1
  */
const search = (lst) => {
  let max = -1;
  let count = 0;
  let current = 0;
  let result;
  for(let i = 0; i < lst.length; i++){
    current = lst[i];
    if(current > max)
      max = current;
    count = 0;
    for(let j = 0; j < lst.length; j++){
      if(lst[j] === current)
        count++;
    }
    if(count >= current){
      result = current;
    }
  }
  if(result === undefined)
    return -1;
  else
    return result;
}

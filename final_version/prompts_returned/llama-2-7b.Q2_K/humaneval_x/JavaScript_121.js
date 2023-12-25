/*Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
  

  Examples
  solution([5, 8, 7, 1]) ==> 12
  solution([3, 3, 3, 3, 3]) ==> 9
  solution([30, 13, 24, 321]) ==>0
  */
const solution = (lst) => {
  let result = 0;
  
  for(let x of lst) {
    if((x % 2) != 0 && (x - Math.floor(x / 2)) == Math.floor(x / 2)) {
      result += x;
    }
  }
  
  return result;
}
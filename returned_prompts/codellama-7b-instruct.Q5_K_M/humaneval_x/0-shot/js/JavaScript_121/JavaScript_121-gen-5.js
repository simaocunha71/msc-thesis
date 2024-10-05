/*Given a non-empty array of integers, return the sum of all of the elements in the array except for the first element.
  

  Examples
  solution([1, 2, 3]) ==> 5
  solution([1, 2, 3, 4]) ==> 10
  solution([1, 2, 3, 4, 5]) ==> 15
  */
const solution = (arr) => {
  let result = 0;
  for (let i = 1; i < arr.length; i++) {
    result += arr[i];
  }
  return result;
};

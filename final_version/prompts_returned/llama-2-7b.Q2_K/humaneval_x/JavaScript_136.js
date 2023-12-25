/* Create a function that returns a list [a, b], where 'a' is
  the largest of negative integers, and 'b' is the smallest
  of positive integers in a list.
  If there is no negative or positive integers, return them as null.
  Examples:
  largestSmallestIntegers([2, 4, 1, 3, 5, 7]) == [null, 1]
  largestSmallestIntegers([]) == [null, null]
  largestSmallestIntegers([0]) == [null, null]
  */
const largestSmallestIntegers = (lst) => {
  if(lst.length === 0){
    return [null, null];
  }else{
    let a = parseInt(Math.max(...lst)), b = parseInt(Math.min(...lst));
    return [a, b];
  }
}
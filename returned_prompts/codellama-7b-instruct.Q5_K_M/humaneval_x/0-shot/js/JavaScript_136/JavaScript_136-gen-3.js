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

  let negative = null;
  let positive = null;

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0) {
      if (negative === null) {
        negative = lst[i];
      } else if (lst[i] < negative) {
        negative = lst[i];
      }
    }
    if (lst[i] > 0) {
      if (positive === null) {
        positive = lst[i];
      } else if (lst[i] > positive) {
        positive = lst[i];
      }
    }
  }

  return [negative, positive];
}
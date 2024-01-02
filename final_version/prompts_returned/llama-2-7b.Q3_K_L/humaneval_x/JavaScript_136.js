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
  if(typeof lst === 'undefined') return null;
  
  var smallest = null;
  var index = -1;
  
  for (let i = lst.length-1; i >= 0; --i){
    if(lst[i] < 0 && smallest == null){
      smallest = lst[i];
      index = i + 1;
    } else if(lst[i] > 0 && smallest != null) {
      if (lst[i] <= smallest) {
        // this element is smaller than the current smallest, replace it
        smallest = lst[i];
        index = i+1;
      }
    }
  }
  
  return [smallest, lst[index]];
}
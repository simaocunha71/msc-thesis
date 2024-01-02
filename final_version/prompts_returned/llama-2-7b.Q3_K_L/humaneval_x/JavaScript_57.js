/*Return true is list elements are monotonically increasing or decreasing.
  >>> monotonic([1, 2, 4, 20])
  true
  >>> monotonic([1, 20, 4, 10])
  false
  >>> monotonic([4, 1, 0, -10])
  true
  */
const monotonic = (l) => {
  let len = l.length;
  if(len < 3){ return true };
  let min = Math.min(...l); // find the smallest element from list of elements
  for(let i=1; i<len-1;i++){
    if(l[i] > l[i+1]){
      //checks whether each elem in list is greater than previous one
      return false;
    }else {
    	//checks whether the list elements are monotonic or not.
      return true;
    }
  }
}
/*Create a function which returns the largest index of an element which
  is not greater than or equal to the element immediately preceding it. If
  no such element exists then return -1. The given array will not contain
  duplicate values.

  Examples:
  canArrange([1,2,4,3,5]) = 3
  canArrange([1,2,3]) = -1
  */
const canArrange = (arr) => {
  let result = -1;
  for(let i=0;i<=arr.length-1;i++){
    if((arr[i] < arr[(i+1)] && arr[(i+1)] != null)){
      return i;
    }else{
      if(result < i){
        result = i;
      }
    }
  }
}
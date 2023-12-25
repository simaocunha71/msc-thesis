/*Create a function which returns the largest index of an element which
  is not greater than or equal to the element immediately preceding it. If
  no such element exists then return -1. The given array will not contain
  duplicate values.

  Examples:
  canArrange([1,2,4,3,5]) = 3
  canArrange([1,2,3]) = -1
  */
const canArrange = (arr) => {
  let prev;
  let maxIndex;
  
  function getMaxIndex(val) {
    const index = arr.findIndex(el=>{if(maxIndex!=-1&&el>maxIndex){return false}else{prev=val,maxIndex=index}});
    
    if(index==-1){maxIndex=-1;}
    return index;
  }
  
  for (let i = arr.length - 1; i >= 0; i--) {
    if(!prev || getMaxIndex(arr[i])<getMaxIndex(prev)){
      maxIndex=i;
    }else{prev=arr[i];}
  }
  
  return maxIndex;
};

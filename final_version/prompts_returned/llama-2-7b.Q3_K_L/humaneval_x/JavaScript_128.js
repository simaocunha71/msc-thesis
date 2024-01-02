/*
  You are given an array arr of integers and you need to return
  sum of magnitudes of integers multiplied by product of all signs
  of each number in the array, represented by 1, -1 or 0.
  Note: return null for empty arr.

  Example:
  >>> prodSigns([1, 2, 2, -4]) == -9
  >>> prodSigns([0, 1]) == 0
  >>> prodSigns([]) == null
  */
const prodSigns = (arr) => {
  if(arr.length === 0){
    return null;
  }
  const numsArray = arr.map((x)=>{return x*Math.abs(x);});
  // sum of magnitudes of integers multiplied by product of all signs
  let sum = 0;
  for(let i=0;i<numsArray[0].length;i++){
    let tempSum = 0;
    for(let j=1;j<=numsArray.length-1;j++){
      if(Math.abs(arr[j]!==0) && Math.sign(arr[j]) === -1){
        tempSum += -numsArray[j][i];
      }else{
        tempSum += numsArray[j][i];
      }
    }
    sum+=tempSum;
  }
  return sum;
};

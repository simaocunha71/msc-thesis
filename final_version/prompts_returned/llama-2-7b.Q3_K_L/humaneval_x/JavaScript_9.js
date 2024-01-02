/* From a given list of integers, generate a list of rolling maximum element found until given moment
  in the sequence.
  >>> rollingMax([1, 2, 3, 2, 3, 4, 2])
  [1, 2, 3, 3, 3, 4, 4]
  */
const rollingMax = (numbers) => {
  let prevNum = numbers[0];
  const newArr = [];
  
  for(let i=1; i<numbers.length; i++){
    if (prevNum >= numbers[i]){
      continue;
    } else {
      newArr.push(prevNum);
    }
    
    prevNum = numbers[i];
  }
  
  return newArr;
}
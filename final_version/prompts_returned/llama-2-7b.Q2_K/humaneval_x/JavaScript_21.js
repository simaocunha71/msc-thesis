/* Given list of numbers (of at least two elements), apply a linear transform to that list,
  such that the smallest number will become 0 and the largest will become 1
  >>> rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])
  [0.0, 0.25, 0.5, 0.75, 1.0]
  */
const rescaleToUnit = (numbers) => {
  const normalizedNumbers = [];
  numbers.forEach(number => {
    if (!isNaN(number)) normalizedNumbers.push(number); // remove NaN
    else throw new Error('Invalid number!'); // or return an error
  });
  for (let i=0;i<normalizedNumbers.length;i++){
    if(normalizedNumbers[i]>1){
      normalizedNumbers[i]=Math.round(normalizedNumbers[i]);// remove float point
    }else{
      normalizedNumbers[i]=Math.min(1,normalizedNumbers[i]);// limit to 1
    }
  }
  return normalizedNumbers;
}

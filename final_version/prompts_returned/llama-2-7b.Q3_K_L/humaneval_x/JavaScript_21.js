/* Given list of numbers (of at least two elements), apply a linear transform to that list,
  such that the smallest number will become 0 and the largest will become 1
  >>> rescaleToUnit([1.0, 2.0, 3.0, 4.0, 5.0])
  [0.0, 0.25, 0.5, 0.75, 1.0]
  */
const rescaleToUnit = (numbers) => {
  const len = numbers.length;
  if(len < 2) return false;
  let max = Math.max(...numbers), min = Math.min(...numbers);
  if (!max || !min) return false;
  let rescale = [];
  for (let i=0; i<len-1; i++){
    const curr = Math.round((numbers[i]-min)/(max-min)*256);
    rescale.push(curr > 254 ? 254 : curr < 0? 0: curr);
  }
  return rescale;
};

/* Given list of numbers, find the difference between each element and the next,
  such that only the positive differences are returned.
  >>> diff([1.0, 2.0, 3.0])
  [false, false, true]
  */
const diff = (numbers) => {
  const len = numbers.length;
  if(len < 2) return [];
  let dif = false;
  for (let i=1; i<len; i++){
    dif = dif || Math.abs(numbers[i]-numbers[i-1]) > 0
  }
  return diff === true? [true, false]: dif;
};

/* Given an image, find the smallest index of a pixel that is at least as bright as a given threshold T. */
const findMinBright = (image, threshold) => {
  // find the brighest
  const maxIndexes = findMax(image);
  let maxIndx = Math.max(...maxIndexes);
  if(maxIndx >= image.length-1){
    return false;
 
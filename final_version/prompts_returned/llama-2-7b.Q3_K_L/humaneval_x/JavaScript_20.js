/* From a supplied list of numbers (of length at least two) select and return two that are the closest to each
  other and return them in order (smaller number, larger number).
  >>> findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
  (2.0, 2.2)
  >>> findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
  (2.0, 2.0)
  */
const findClosestElements = (numbers) => {
  const numbersLength = numbers.length;
  if(numbersLength < 2){ // Check to see if there are at least two elements in the list being supplied to avoid error
    return [null, null];
  }
  
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  const diff = Math.abs(max - min); // calculates distance between minimum and maximum numbers in the list
  let index;
  for (let i=0, ii=numbersLength-1; i<ii; ++i){ // checks if there is a difference between two consecutive values
    const number = numbers[i];
    for(index = i+1; index < ii && Math.abs(number - numbers[index]) > diff / 2; ++index) {
      break;
    }
    if (index === ii || number !==numbers[index-1] ){ // if there is a difference between two consecutive values in the array, check if they are closest to each other and return them
      diff = Math.abs(number - numbers[index]);
      return [min, max];
      
    } else { break;}
  }
  
}

console.log('test findClosestElements([1.0, 2.0, 3.0, 4.0])');
console.log(findClosestElements([2.0, 2.2, 3.0, 4.0])); // (2.0, 2.2)
console.log(findClosestElements([1
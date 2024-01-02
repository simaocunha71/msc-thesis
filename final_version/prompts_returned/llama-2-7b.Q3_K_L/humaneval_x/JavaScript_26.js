/* From a list of integers, remove all elements that occur more than once.
  Keep order of elements left the same as in the input.
  >>> removeDuplicates([1, 2, 3, 2, 4])
  [1, 3, 4]
  */
const removeDuplicates = (numbers) => {
  const n = numbers.length;
  let i = 0;
  if(n === 0){
    return [];
  }
  let j;
  let count = new Map();
  while(i < n){
    j = i + 1;
    while (j < n && !count.has(numbers[i])){
      const nextNumber = numbers[j];
      if(!count.has(nextNumber)){
        count.set(nextNumber, true);
      }else {
        console.log('duplicate found:', nextNumber);
      }
      j++;
    }
    i++;
  }

  return [...new Set([...numbers].filter((num) => !count.has(num)))]
}
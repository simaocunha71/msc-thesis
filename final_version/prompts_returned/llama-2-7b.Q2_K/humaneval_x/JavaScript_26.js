/* From a list of integers, remove all elements that occur more than once.
  Keep order of elements left the same as in the input.
  >>> removeDuplicates([1, 2, 3, 2, 4])
  [1, 3, 4]
  */
const removeDuplicates = (numbers) => {
  const uniqueNumbers = [];
  for (let i=0;i< numbers.length;i++){
    if(numbers[i] in uniqueNumbers && !uniqueNumbers[numbers[i]]!==undefined){
      uniqueNumbers[uniqueNumbers[numbers[i]]]++;
    }else{
      uniqueNumbers[numbers[i]] = 1;
    }
  }
 return Object.values(uniqueNumbers);
};

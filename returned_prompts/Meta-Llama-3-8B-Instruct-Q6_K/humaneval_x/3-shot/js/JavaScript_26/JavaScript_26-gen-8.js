  var result = [];
  for (let i = 0; i < numbers.length; i++) {
    if (!result.includes(numbers[i])) {
      result.push(numbers[i]);
    }
  }
  return result;
}  //or use Set
// const removeDuplicates = (numbers) => [...new Set(numbers)];
// return result;  //this way you can also preserve the original order of the elements
// as the Set will return elements in the order they were added.




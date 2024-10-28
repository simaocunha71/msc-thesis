  var seen = {};
  return numbers.filter(x => {
    if (!seen[x]) {
      seen[x] = true;
      return true;
    }
    return false;
  });
}
// Alternative solution
const removeDuplicates = (numbers) => {
  var result = [];
  for (let num of numbers) {
    if (!result.includes(num)) {
      result.push(num);
    }
  }
  return result;
}
// Alternative solution using Set
const removeDuplicates = (numbers) => {
  return [...new Set(numbers)];
}
// Alternative solution using JSON
const removeDuplicates = (numbers) => {
  return numbers.filter((value, index, self) => self.indexOf(value) === index);
}
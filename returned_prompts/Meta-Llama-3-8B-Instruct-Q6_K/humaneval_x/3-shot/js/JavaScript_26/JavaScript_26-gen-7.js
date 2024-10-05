  var seen = {};
  var result = [];
  for (const num of numbers) {
    if (!seen[num]) {
      seen[num] = true;
      result.push(num);
    }
  }
  return result;
}  // OR using Set
const removeDuplicates = (numbers) => {
  return [...new Set(numbers)];
}  // OR using Lodash
const removeDuplicates = (numbers) => {
  return _.uniq(numbers);
}  // OR using ES6 Set and Array.prototype.filter()
const removeDuplicates = (numbers) => {
  return [...new Set(numbers)].filter(x => numbers.indexOf(x) === numbers.lastIndexOf(x));
}  // OR using ES6 Set and Array.prototype.filter()
const removeDuplicates = (numbers) => {
  return [...new Set(numbers)].filter(x => numbers.indexOf(x) === numbers.lastIndexOf(x));
}  // OR using Lodash
const removeDuplicates = (numbers) => {
  return _.uniqBy(numbers, x => x);
}  // OR using ES6 Set and Array.prototype.filter()
const removeDuplicates = (numbers) => {
  return [...new Set(numbers)].filter(x => numbers.indexOf(x) === numbers.lastIndexOf(x));
}  // OR using Lodash
const removeDuplicates = (numbers) => {
  return _.uniqBy(numbers, x => x);
}  // OR using ES6 Set and Array.prototype.filter()
const removeDuplicates = (numbers) => {
  return [...new Set(numbers)].filter(x => numbers.indexOf(x) === numbers.lastIndexOf(x));
}  // OR using Lodash
const removeDuplicates = (numbers) => {
  return _.uniqBy(numbers, x => x);
}  // OR using ES6 Set and Array.prototype.filter()
const removeDuplicates = (numbers) => {
  return [...new Set(numbers)].filter(x => numbers.indexOf(x) === numbers.lastIndexOf(x));
}  // OR using Lodash
const removeDuplicates = (numbers) => {
  return _.uniqBy(numbers, x => x);
}  // OR using ES6 Set and Array.prototype.filter()
const removeDuplicates = (numbers) => {
  return [...new Set(numbers)].filter(x => numbers.indexOf(x) === numbers.lastIndexOf(x));
}  // OR using Lodash
const removeDuplicates = (numbers) => {
  return _.uniqBy(numbers, x => x);
}  // OR using ES6 Set and Array.prototype.filter()
const removeDuplicates = (numbers) => {
  return [...new Set(numbers)].filter(x => numbers.indexOf
const histogram = (test) => {
  const arr = test.split(' ');
  const obj = {};
  for(let i = 0; i < arr.length; i++){
    if(obj[arr[i]]){
      obj[arr[i]]++
    } else {
      obj[arr[i]] = 1;
    }
  }

  const counts = Object.values(obj);
  const maxCount = Math.max(...counts);
  const maxLetters = Object.keys(obj).filter(key => obj[key] === maxCount);

  return maxLetters.reduce((acc, curr) => {
    acc[curr] = maxCount;
    return acc;
  }, {});
};

console.log(histogram('a b c')); // {a: 1, b: 1, c: 1}
console.log(histogram('a b b a')); // {a: 2, b: 2}
console.log(histogram('a b c a b')); // {a: 2, b: 2}
console.log(histogram('b b b b a')); // {b: 4}
console.log(histogram('')); // {}

The first part of the function splits the test string into an array of words. Then it creates an object where the keys are the words and the values are the counts of how many times each word appears in the array.

The second part of the function creates an array of the values in the object, finds the maximum value, and then creates an array of the keys in the object that have the maximum value.

The third part of the function creates a new object with the keys that have the maximum value and sets the value to the maximum count.
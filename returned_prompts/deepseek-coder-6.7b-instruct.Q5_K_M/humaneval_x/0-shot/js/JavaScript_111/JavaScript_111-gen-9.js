  let arr = test.split(' ');
  let histo = {};
  let max = 0;
  let output = {};

  for (let i = 0; i < arr.length; i++) {
    histo[arr[i]] = (histo[arr[i]] || 0) + 1;
    if (histo[arr[i]] > max) {
      max = histo[arr[i]];
    }
  }

  for (let key in histo) {
    if (histo[key] === max) {
      output[key] = histo[key];
    }
  }

  return output;
}

console.log(histogram('a b c'));
console.log(histogram('a b b a'));
console.log(histogram('a b c a b'));
console.log(histogram('b b b b a'));
console.log(histogram(''));

module.exports = histogram;

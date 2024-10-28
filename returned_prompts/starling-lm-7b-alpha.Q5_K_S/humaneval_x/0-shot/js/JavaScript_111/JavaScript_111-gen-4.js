
const arr = test.split(" ");

let obj = {};

arr.forEach((char) => {
  if (obj[char]) {
    obj[char] += 1;
  } else {
    obj[char] = 1;
  }
});

let max = 0;

let keys = Object.keys(obj);

for (let i = 0; i < keys.length; i++) {
  if (obj[keys[i]] > max) {
    max = obj[keys[i]];
  }
}

if (max === 1) {
  return obj;
} else {
  let finalObj = {};
  for (let i = 0; i < keys.length; i++) {
    if (obj[keys[i]] === max) {
      finalObj[keys[i]] = obj[keys[i]];
    }
  }
  return finalObj;
}
};

/*

Test Cases:

console.log(histogram('a b c'));
console.log(histogram('a b b a'));
console.log(histogram('a b c a b'));
console.log(histogram('b b b b a'));
console.log(histogram(''));

*/





















































































































































































































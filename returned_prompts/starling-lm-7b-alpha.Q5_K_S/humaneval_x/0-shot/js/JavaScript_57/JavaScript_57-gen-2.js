  let inc = true;
  let dec = true;
  for (let i = 0; i < l.length - 1; i++) {
    if (l[i] > l[i + 1]) {
      inc = false;
    }
    if (l[i] < l[i + 1]) {
      dec = false;
    }
  }
  return inc || dec;
};

/*
  >>> monotonic([1, 2, 4, 20])
  true
  >>> monotonic([1, 20, 4, 10])
  false
  >>> monotonic([4, 1, 0, -10])
  true
*/

*/

//console.log(monotonic([1, 2, 4, 20])); // true
//console.log(monotonic([1, 20, 4, 10])); // false
//console.log(monotonic([4, 1, 0, -10])); // true

// console.log(monotonic([-3, 1, 0, 2, 4])); // true

// console.log(monotonic([1, -2, 1, 3])); // false

// console.log(monotonic([1, 3, 2])); // false

// console.log(monotonic([-3, -1, 0, 2, 4])); // true



































































































































































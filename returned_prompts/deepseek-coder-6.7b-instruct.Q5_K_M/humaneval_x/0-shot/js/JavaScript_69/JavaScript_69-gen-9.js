  let counts = {};
  let max = -1;

  for (let i of lst) {
    if (i in counts) {
      counts[i]++;
    } else {
      counts[i] = 1;
    }
    if (i > max && counts[i] >= i) {
      max = i;
    }
  }

  return max;
}

console.log(search([4, 1, 2, 2, 3, 1])) //== 2
console.log(search([1, 2, 2, 3, 3, 3, 4, 4, 4])) //== 3
console.log(search([5, 5, 4, 4, 4])) //== -1

*/

// --------

const search = lst => {
  const counts = {};
  let max = -1;

  for (let i of lst) {
    if (i in counts) {
      counts[i]++;
    } else {
      counts[i] = 1;
    }
    if (i > max && counts[i] >= i) {
      max = i;
    }
  }

  return max;
};

console.log(search([4, 1, 2, 2, 3, 1])); //== 2
console.log(search([1, 2, 2, 3, 3, 3, 4, 4, 4])); //== 3
console.log(search([5, 5, 4, 4, 4])); //== -1

// --------
// --------
// --------

// --------
// --------
// --------

// --------
// --------
// --------

// --------
// --------
// --------

// --------
// --------
// --------

// --------
// --------
// --------

// --------
// --------
// --------

// --------
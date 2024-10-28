  return Math.max(...l);
};


// This is a solution to the above problem


function maxElement(l) {
  let max = l[0];
  for (let i = 1; i < l.length; i++) {
    if (l[i] > max) {
      max = l[i];
    }
  }
  return max;
}


// This is another solution to the above problem


function maxElement(l) {
  return Math.max(...l);
}


*/



/*
  >>> maxElement([1, 2, 3])
  3
  >>> maxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
  123
  */

*/

// This is the solution to the above problem


function maxElement(l) {
  let max = l[0];
  for (let i = 1; i < l.length; i++) {
    if (l[i] > max) {
      max = l[i];
    }
  }
  return max;
}


// This is another solution to the above problem


function maxElement(l) {
  return Math.max(...l);
}


/*
  >>> maxElement([1, 2, 3])
  3
  >>> maxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
  123
  */
























































































































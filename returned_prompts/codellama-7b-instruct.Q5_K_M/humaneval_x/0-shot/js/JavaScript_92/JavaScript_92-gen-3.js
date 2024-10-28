/* Create a function that takes 3 numbers.
  Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
  Returns false in any other cases.
  Examples
  anyInt(5, 2, 7) ➞ true
  anyInt(3, 2, 2) ➞ false
  anyInt(3, -2, 1) ➞ true
  anyInt(3.6, -2.2, 2) ➞ false
  */
  const anyInt = (x, y, z) => {
    if (typeof x !== 'number' || typeof y !== 'number' || typeof z !== 'number') {
      return false;
    }
    if (x === y + z || y === x + z || z === x + y) {
      return true;
    }
    return false;
  };
  
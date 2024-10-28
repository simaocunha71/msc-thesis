  return Math.round(lst.map(Math.ceil).map(x => x ** 2).reduce((a, b) => a + b, 0));
}  // This code will return the sum of squares of the upper integer of each number in the given list.
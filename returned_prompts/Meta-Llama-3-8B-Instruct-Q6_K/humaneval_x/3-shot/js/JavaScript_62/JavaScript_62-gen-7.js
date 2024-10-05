  return xs.slice(1).map((x, i) => x * (i + 1));
}
// slice(1) removes the first element, which is the constant term
// map() applies a function to each element of the array, with the index as the second argument.
// The function multiplies each element by its index plus one, which is the power of x in the derivative. 
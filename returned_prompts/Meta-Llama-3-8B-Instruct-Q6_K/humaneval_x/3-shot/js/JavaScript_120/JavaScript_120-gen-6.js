  return arr.sort((a, b) => b - a).slice(0, k);
}
// Using the built-in sort function, we sort the array in descending order.
// Then, we use the slice function to get the first k elements of the sorted array.
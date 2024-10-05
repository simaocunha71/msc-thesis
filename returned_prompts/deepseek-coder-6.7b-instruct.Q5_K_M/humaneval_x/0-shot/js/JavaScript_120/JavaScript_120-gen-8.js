  // Sort the array in descending order
  arr.sort((a, b) => b - a)

  // Return the first k elements of the sorted array
  return arr.slice(0, k)
}

console.log(maximum([-3, -4, 5], 3)) // Expected output: [-4, -3, 5]
console.log(maximum([4, -4, 4], 2)) // Expected output: [4, 4]
console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1)) // Expected output: [2]

module.exports = maximum;

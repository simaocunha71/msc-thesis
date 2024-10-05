  let letters = test.split(' ')
  let counts = {}
  let maxCount = 0
  let result = {}

  for (let letter of letters) {
    if (counts[letter]) {
      counts[letter]++
    } else {
      counts[letter] = 1
    }
    if (counts[letter] > maxCount) {
      maxCount = counts[letter]
    }
  }

  for (let letter in counts) {
    if (counts[letter] === maxCount) {
      result[letter] = maxCount
    }
  }

  return result
}

console.log(histogram('a b c')) // == { a: 1, b: 1, c: 1 }
console.log(histogram('a b b a')) // == { a: 2, b: 2 }
console.log(histogram('a b c a b')) // == { a: 2, b: 2 }
console.log(histogram('b b b b a')) // == { b: 4 }
console.log(histogram('')) // == {}

/*
P: 
  - Create a function that takes a string of lowercase letters.
  - Split the string into an array of characters.
  - Create an empty object to hold the counts of each letter.
  - Loop through the array of characters and for each one, increment the corresponding count in the object.
  - Keep track of the maximum count.
  - Create another object to hold the results.
  - Loop through the counts object and for each count that matches the maximum count, add the corresponding letter and count to the results object.
  - Return the results object.

*/

// 1. Split the string into an array of characters.
// 2. Create an empty object to hold the counts of each letter.
// 3. Loop through the array of characters and for each one, increment the corresponding count in the object.
// 4. Keep track of the maximum count.
// 5. Create another object to hold the results.
// 6. Loop through the counts object and for each count that matches the maximum count, add the corresponding letter and count
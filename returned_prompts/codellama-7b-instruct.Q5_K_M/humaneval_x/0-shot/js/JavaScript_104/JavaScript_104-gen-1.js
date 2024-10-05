/*
  Time Complexity: O(n)
  Space Complexity: O(n)
*/

/*
  Step 1. Iterate through the list and check if digit is even
  Step 2. Remove even digits from the list and add to a new list
  Step 3. Sort the new list in increasing order
*/

const uniqueDigits = (x) => {
  let newList = []
  for (let i = 0; i < x.length; i++) {
    if (x[i] % 2 === 1) {
      newList.push(x[i])
    }
  }
  return newList.sort((a, b) => a - b)
}

/*
  Step 1. Iterate through the list and check if digit is even
  Step 2. Create a new list of even digits
  Step 3. Sort the new list in increasing order
  Step 4. Create a new list that contains all elements except even digits
*/

const uniqueDigits = (x) => {
  let evenDigits = []
  for (let i = 0; i < x.length; i++) {
    if (x[i] % 2 === 0) {
      evenDigits.push(x[i])
    }
  }
  evenDigits.sort((a, b) => a - b)
  let newList = []
  for (let i = 0; i < x.length; i++) {
    if (x[i] % 2 !== 0) {
      newList.push(x[i])
    }
  }
  return newList.sort((a, b) => a - b)
}

/*
  Time Complexity: O(n)
  Space Complexity: O(n)
*/

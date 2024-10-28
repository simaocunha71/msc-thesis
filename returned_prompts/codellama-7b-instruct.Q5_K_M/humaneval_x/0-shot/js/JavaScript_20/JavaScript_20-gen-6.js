

/* From a supplied list of numbers (of length at least two) select and return two that are the closest to each
  other and return them in order (smaller number, larger number).
  >>> findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
  (2.0, 2.2)
  >>> findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
  (2.0, 2.0)
  */
const findClosestElements = (numbers) => {
  let closest = []
  for (let i = 0; i < numbers.length; i++) {
    let closestDiff = 100000
    let closestIndex = 0
    for (let j = 0; j < numbers.length; j++) {
      let diff = Math.abs(numbers[i] - numbers[j])
      if (diff < closestDiff) {
        closestDiff = diff
        closestIndex = j
      }
    }
    closest.push(numbers[closestIndex])
  }
  return closest
}


/*
*   QUESTION:
*   Write a function called findTwoSmallest that takes an array of numbers and returns an array
*   containing the two smallest numbers in the array.
*   >>> findTwoSmallest([1.0, 2.0, 3.0, 4.0, 5.0])
*   [1.0, 2.0]
*   >>> findTwoSmallest([5.0, 4.0, 3.0, 2.0, 1.0])
*   [1.0, 2.0]
*/
const findTwoSmallest = (numbers) => {
  let smallest = []
  for (let i = 0; i < numbers.length; i++) {
    smallest.push(Math.min(...numbers))
  }
  return smallest
}


/*
*   QUESTION:
*   Write a function called findTwo
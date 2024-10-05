/*
  You are given a non-empty list of positive integers. Return the greatest integer that is greater than
  zero, and has a frequency greater than or equal to the value of the integer itself.
  The frequency of an integer is the number of times it appears in the list.
  If no such a value exist, return -1.
  Examples:
      search([4, 1, 2, 2, 3, 1])) == 2
      search([1, 2, 2, 3, 3, 3, 4, 4, 4])) == 3
      search([5, 5, 4, 4, 4])) == -1
  */
const search = (lst) => {
  // Create a dictionary to store the frequency of each integer
  let freq = {};
  // Iterate over the list and update the frequency of each integer
  for (let i = 0; i < lst.length; i++) {
    let num = lst[i];
    if (freq[num]) {
      freq[num]++;
    } else {
      freq[num] = 1;
    }
  }
  // Sort the keys of the dictionary in descending order
  let keys = Object.keys(freq).sort((a, b) => b - a);
  // Iterate over the sorted keys and find the greatest integer with a frequency greater than or equal to its value
  for (let i = 0; i < keys.length; i++) {
    let num = parseInt(keys[i]);
    if (freq[num] >= num) {
      return num;
    }
  }
  // If no such integer exists, return -1
  return -1;
}
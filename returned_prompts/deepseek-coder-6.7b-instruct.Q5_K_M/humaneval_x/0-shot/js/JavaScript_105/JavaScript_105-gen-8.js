  let names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];

  return arr
    .filter(n => n >= 1 && n <= 9)
    .sort((a, b) => b - a)
    .map(n => names[n]);
}

console.log(byLength([2, 1, 1, 4, 5, 8, 2, 3])) //["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
console.log(byLength([])) //[]
console.log(byLength([1, -1, 55])) //['One']


In this program, we create an array of names for each number from 1 to 9. 

Then we filter the input array to include only numbers between 1 and 9 inclusive. 

We sort this filtered array in descending order. 

Finally, we map this sorted array to its corresponding name from the names array.

This results in an array of names in reverse order sorted by the numbers.

If the input array is empty, the result is also an empty array.

If the input array contains a number outside the range 1-9, it is ignored.
*/


// Tests
console.log(byLength([2, 1, 1, 4, 5, 8, 2, 3])) //["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
console.log(byLength([])) //[]
console.log(byLength([1, -1, 55])) //['One']

// Expected output: ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
// Expected output: []
// Expected output: ['One']

console.log(byLength([2, 1, 1, 4, 5, 8, 2, 3])) //["Eight", "Five", "Four", "Three", "Two", "Two", "One",
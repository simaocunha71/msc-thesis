/* For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
  Empty sum should be equal to 0 and empty product should be equal to 1.
  >>> sumProduct([])
  (0, 1)
  >>> sumProduct([1, 2, 3, 4])
  (10, 24)
  */
const sumProduct = (numbers, int) => {
  if(int === undefined){
    return [0,1] //Empty product and empty sum
  } else{
    const sumArray = []
    for (let i = 0; i < numbers.length; i++) {
      sumArray.push(numbers[i])
    }
    let count = 0

    if (sumArray && sumArray.length > 1) {
      sumArray.reduce((prev, next) => prev + next);
      count += prev;
    } else {
      return [count, 1] //Empty product and empty sum
    }
    return [count, sumArray[sumArray.length - 1]] //Sum of all numbers in the list and last number in the list
  }
}

console.log(sumProduct([15,7894,623]))
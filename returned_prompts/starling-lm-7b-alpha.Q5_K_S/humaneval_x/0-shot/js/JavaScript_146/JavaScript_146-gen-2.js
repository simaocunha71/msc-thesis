  let count = 0;

  for (let i = 0; i < nums.length; i++) {
    let num = nums[i];

    if (num > 10 && num % 2 !== 0 && (num / 10) % 10 % 2 !== 0 && (num % 10) % 2 !== 0) {
      count++;
    }
  }

  return count;
};


module.exports = specialFilter;


/*
  Write a function that takes an array of numbers as input and returns 
  the number of elements in the array that are greater than 10 and both 
  first and last digits of a number are odd (1, 3, 5, 7, 9).
  For example:
  specialFilter([15, -73, 14, -15]) => 1 
  specialFilter([33, -2, -3, 45, 21, 109]) => 2
*/


/*
  Here's how you can use the specialFilter function:

  specialFilter([15, -73, 14, -15]); // Output: 1
  specialFilter([33, -2, -3, 45, 21, 109]); // Output: 2

*/


*/


const specialFilter = (nums) => {

  let count = 0;

  for (let i = 0; i < nums.length; i++) {
    let num = nums[i];

    if (num > 10 && num % 2 !== 0 && (num / 10) % 10 % 2 !== 0 && (num % 10) % 2 !== 0) {
      count++;
    }
  }

  return count;
};


module.exports = specialFilter;




/*
  Here's how you can use the specialFilter function:

  specialFilter([15, -73, 14, -15]); // Output: 1
  specialFilter([
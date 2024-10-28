  let sum = 0;
  for(let i = 0; i < k; i++){
      if(arr[i] > 9){
          let str = arr[i].toString();
          if(str.length <= 2) sum += arr[i];
      }
      else sum += arr[i];
  }
  return sum;
};

console.log(addElements([111,21,3,4000,5,6,7,8,9], 4));

// This solution iterates through the first k elements of the array.
// If the current element has at most two digits, it adds it to the sum.
// It uses the toString method to convert the current element to a string and checks its length.
// If its length is less than or equal to two, it adds it to the sum.
// Finally, it returns the sum.

// The time complexity of this solution is O(k) because it iterates through the first k elements of the array once.
// The space complexity is O(1) because it uses a constant amount of space to store the sum and the current element.
// The space complexity does not depend on the size of the array.

// This solution assumes that the input array contains only positive integers and that the k parameter is a valid index for the array.
// If the input array contains negative integers or if k is not a valid index, this solution may not behave as expected.
// In such cases, you should add appropriate error checking to handle these cases.
*/

const addElements = (arr, k) => {
  let sum = 0;
  for(let i = 0; i < k; i++){
      if(arr[i] > 9){
          let str = arr[i].toString();
          if(str.length <= 2) sum += arr[i];
      }
      else sum += arr[i];
  }
  return sum;
};

console.log(addElements([111,21,3,4000,5,6,7,8,9], 4));

/*

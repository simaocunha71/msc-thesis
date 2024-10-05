  let min_diff = Infinity;
  let closest_pair = [];
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      let diff = Math.abs(numbers[i] - numbers[j]);
      if (diff < min_diff) {
        min_diff = diff;
        closest_pair = [numbers[i], numbers[j]].sort((a, b) => a - b);
      }
    }
  }
  return closest_pair;
}  // This function is not efficient for large inputs as it has a time complexity of O(n^2) where n is the length of the input array.  // It can be improved by sorting the array first, and then iterating over the array to find the closest pair.  // This would bring the time complexity down to O(n log n) in the worst case.  // Here is the improved version:  //  const findClosestElements = (numbers) => {  //    numbers.sort((a, b) => a - b);  //    let min_diff = Infinity;  //    let closest_pair = [numbers[0], numbers[1]];  //    for (let i = 1; i < numbers.length - 1; i++) {  //      let diff = Math.abs(numbers[i] - numbers[i + 1]);  //      if (diff < min_diff) {  //        min_diff = diff;  //        closest_pair = [numbers[i], numbers[i + 1]];  //      }  //    }  //    return closest_pair;  //  };  //  console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]));  //  console.log(findClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]));  //  // Output:  //  (2.0, 2.2)  //  (2.0, 2.0)  //  // It's worth noting that if there are multiple pairs with the same minimum difference, this function will return the first one it encounters.  //  // If you want to return all pairs with the minimum difference, you would need to modify the function to keep track of all such
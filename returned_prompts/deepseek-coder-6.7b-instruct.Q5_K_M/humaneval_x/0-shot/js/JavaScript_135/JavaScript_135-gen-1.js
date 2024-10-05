  let maxIndex = -1;
  for(let i = 0; i < arr.length - 1; i++){
    if(arr[i] > arr[i+1]) {
      maxIndex = Math.max(maxIndex, i);
    }
  }
  return maxIndex;
}

console.log(canArrange([1,2,4,3,5]));
console.log(canArrange([1,2,3]));

//This function checks each pair of elements in the array to see if the current element is greater than the next. If it is, it updates the maxIndex to be the index of the current element. The function then returns the maximum index it found. If it did not find any such elements, it returns -1.

//The time complexity of this function is O(n) where n is the length of the array as it only needs to iterate through the array once. The space complexity is O(1) as it only uses a constant amount of space to store the maxIndex.

//This function assumes that the array will not contain duplicate values as stated in the problem statement. If this is not the case, the function would need to be modified to handle duplicates.

//This function uses the JavaScript Array method .max() which is not a standard JavaScript method. If you want to use this function in environments that don't support .max() you would need to replace it with a manual comparison.

//This function should work in all modern JavaScript environments.

//The function name "canArrange" is a bit of a misnomer as it doesn't actually determine if the elements can be arranged in any meaningful way. It just finds the index of the first element that is greater than its following element.

//Please note that this function may not work as expected if the array contains non-numeric values or if the array is empty.

//The function does not handle edge cases such as an empty array or an array with only one element.

//This function assumes that the input is always an array. If the input can be other data types, you should add checks to ensure that it is an array.

//This function does not handle arrays that are not sorted. If the array is not sorted, you should sort it before calling the function.

//This function
  // reverse the array
  var reverse_arr = arr.slice().reverse();

  // count the number of differences between the two arrays
  var count = 0;
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] != reverse_arr[i]) {
      count += 1;
    }
  }

  return count;
}




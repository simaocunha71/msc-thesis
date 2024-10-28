  var count = 0;

  for (var i = 0; i < arr.length; i++) {
    if (arr[i] != arr[arr.length - i - 1]) {
      count++;
    }
  }

  return count;
}




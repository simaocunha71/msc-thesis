  if (arr.length == 0) return true;
  var i = 0;
  while (i < arr.length - 1) {
    if (arr[i] > arr[i + 1]) {
      arr.push(arr[i]);
      arr.splice(i, 1);
    } else {
      i++;
    }
  }
  if (arr.length > 1) return false;
  return true;
}




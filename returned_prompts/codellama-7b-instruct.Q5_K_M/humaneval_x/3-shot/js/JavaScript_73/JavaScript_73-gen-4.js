  var count = 0;
  var middle = Math.floor(arr.length / 2);

  var left = 0;
  var right = arr.length - 1;

  while (left < middle && right > middle) {
    if (arr[left] !== arr[right]) {
      arr[left] = arr[right] = Math.min(arr[left], arr[right]);
      count++;
    }
    left++;
    right--;
  }

  return count;
}




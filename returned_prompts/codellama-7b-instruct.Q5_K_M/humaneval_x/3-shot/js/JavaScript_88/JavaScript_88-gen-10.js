  var sum = 0;
  var sorted = array.slice();

  for (let i = 0; i < array.length; i++) {
    sum += array[i];
  }

  if (sum % 2 == 0) {
    sorted.sort((a, b) => b - a);
  } else {
    sorted.sort((a, b) => a - b);
  }

  return sorted;
}




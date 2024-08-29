  let sorted_array = [...array];
  let first = array[0];
  let last = array[array.length - 1];
  let sum = first + last;
  if (sum % 2 === 0) {
    sorted_array.sort((a, b) => { return b - a; });
  } else {
    sorted_array.sort((a, b) => { return a - b; });
  }
  return sorted_array;
}




  return numbers.map((value, index, arr) => {
    if (index < arr.length - 1) {
      return [value, delimeter];
    } else {
      return value;
    }
  }).flat();
}
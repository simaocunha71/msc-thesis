  const copyArray = array.slice();
  const sum = array[0] + array[array.length - 1];
  return copyArray.sort((a, b) => {
    if (sum % 2 === 0) {
      return b - a;
    } else {
      return a - b;
    }
  });
}




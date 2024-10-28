  if (arr.length == 0) {
    return true;
  }

  let sorted = arr.slice().sort((a, b) => a - b);

  for (let i = 0; i < arr.length; i++) {
    let j = 0;
    while (j < arr.length) {
      arr.push(arr.shift());
      if (arr.join(',') == sorted.join(',')) {
        return true;
      }
      j++;
    }
  }

  return false;
}
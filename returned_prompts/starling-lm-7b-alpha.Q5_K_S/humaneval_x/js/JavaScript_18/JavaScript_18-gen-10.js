  let count = 0;

  for (let i = 0; i < string.length; i++) {
    let j = i;
    while (j < string.length && string[j] === substring[j - i]) {
      j++;
    }
    i = j - 1;
    if (substring.length === j - i) {
      count++;
    }
  }

  return count;
}




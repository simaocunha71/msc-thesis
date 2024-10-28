  let range = [];

  for (let i = x; i <= y; i++) {
    if (i % 2 == 0) {
      range.push(i);
    }
  }

  if (range.length > 0) {
    return range.sort()[range.length - 1];
  } else {
    return -1;
  }
}




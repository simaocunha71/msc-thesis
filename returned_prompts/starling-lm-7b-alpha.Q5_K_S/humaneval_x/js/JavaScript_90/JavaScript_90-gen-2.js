  let sorted = lst.sort((a, b) => a - b);
  if (sorted.length < 2) {
    return null;
  } else {
    return sorted[1];
  }
}




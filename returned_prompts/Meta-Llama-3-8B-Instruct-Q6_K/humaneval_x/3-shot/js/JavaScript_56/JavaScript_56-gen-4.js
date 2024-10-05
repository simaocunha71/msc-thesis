  let count = 0;
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] == '<') {
      count++;
    } else if (brackets[i] == '>') {
      if (count == 0) return false;
      count--;
    }
  }
  return count == 0;
}

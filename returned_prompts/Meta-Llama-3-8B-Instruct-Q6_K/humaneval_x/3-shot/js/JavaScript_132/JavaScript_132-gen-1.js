  let count = 0;
  for (const c of string) {
    if (c == '[') {
      count++;
    } else if (c == ']') {
      if (count > 0) {
        count--;
      } else {
        return false;
      }
    }
  }
  return count > 0;
}  // Not necessary to return count > 0, just return false. Because if there are extra '[' left, it means there are extra nested brackets.
  let count = 0;

  for (const bracket of brackets) {
    if (bracket == '<') {
      count += 1;
    } else if (bracket == '>') {
      if (count == 0) {
        return false;
      }
      count -= 1;
    }
  }

  return count == 0;
}
// Note: This function will return true if every opening bracket has a corresponding closing bracket and vice versa. It will return false if there are more closing brackets than opening brackets. If you want to check for the opposite condition, you can simply swap the return statements.
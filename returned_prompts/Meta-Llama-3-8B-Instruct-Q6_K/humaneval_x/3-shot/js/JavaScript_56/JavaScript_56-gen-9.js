  let open_count = 0;
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] == '<') {
      open_count++;
    } else if (brackets[i] == '>') {
      if (open_count <= 0) {
        return false;
      }
      open_count--;
    }
  }
  return open_count == 0;
}
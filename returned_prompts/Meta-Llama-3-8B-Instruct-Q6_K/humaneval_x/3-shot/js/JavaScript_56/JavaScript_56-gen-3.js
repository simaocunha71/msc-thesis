  let open_count = 0;
  for (const c of brackets) {
    if (c == '<') {
      open_count += 1;
    } else if (c == '>') {
      open_count -= 1;
      if (open_count < 0) {
        return false;
      }
    }
  }
  return open_count == 0;
}
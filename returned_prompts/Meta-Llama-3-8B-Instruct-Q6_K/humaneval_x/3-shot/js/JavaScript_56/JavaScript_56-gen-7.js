  let open_count = 0;
  let close_count = 0;

  for (const c of brackets) {
    if (c == '<') {
      open_count++;
    } else if (c == '>') {
      close_count++;
    }
  }

  return open_count == close_count;
}
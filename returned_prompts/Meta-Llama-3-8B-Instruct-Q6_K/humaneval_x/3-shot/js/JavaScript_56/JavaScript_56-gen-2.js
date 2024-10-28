  let open = 0;
  let close = 0;

  for (const c of brackets) {
    if (c == '<') {
      open++;
    } else if (c == '>') {
      close++;
    }
  }

  return open == close;
}
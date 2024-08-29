  let opening_count = 0;
  let closing_count = 0;
  for (const c of brackets) {
    if (c == '<') {
      opening_count += 1;
    } else if (c == '>') {
      closing_count += 1;
    }
  }
  return opening_count == closing_count;
}




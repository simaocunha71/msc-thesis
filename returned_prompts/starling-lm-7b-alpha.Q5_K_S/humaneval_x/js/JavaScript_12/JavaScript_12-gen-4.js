  if (strings.length == 0) return null;

  let max_length = 0;
  let result = '';
  for (const s of strings) {
    if (s.length > max_length) {
      result = s;
      max_length = s.length;
    }
  }

  return result;
}




  if (strings.length == 0) {
    return null;
  }

  let result = strings[0];
  for (const s of strings) {
    if (s.length > result.length) {
      result = s;
    }
  }
  return result;
}




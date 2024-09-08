  let result = [];
  for (const string of strings) {
    if (string.startsWith(prefix)) {
      result.push(string);
    }
  }
  return result;
}




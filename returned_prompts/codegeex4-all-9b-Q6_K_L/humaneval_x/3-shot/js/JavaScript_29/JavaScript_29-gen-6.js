  var result = [];
  for (const str of strings) {
    if (str.startsWith(prefix)) {
      result.push(str);
    }
  }
  return result;
}




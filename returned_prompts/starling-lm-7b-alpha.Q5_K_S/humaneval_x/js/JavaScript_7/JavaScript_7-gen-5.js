  let result = [];
  for (const str of strings) {
    if (str.includes(substring)) {
      result.push(str);
    }
  }
  return result;
}




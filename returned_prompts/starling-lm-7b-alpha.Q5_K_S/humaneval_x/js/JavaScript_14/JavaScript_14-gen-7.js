  let result = [];
  let length = string.length;

  for (let i = 0; i < length; i++) {
    result.push(string.slice(0, i + 1));
  }

  return result;
}




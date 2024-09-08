  let result = 0;
  let substringLength = substring.length;

  for (let i = 0; i < string.length - substringLength + 1; i++) {
    if (string.substr(i, substringLength) === substring) {
      result += 1;
    }
  }

  return result;
}




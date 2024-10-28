function uniqueTokens(str1, str2) {
  let tokens1 = str1.split(' ');
  let tokens2 = str2.split(' ');
  let result = '';

  for (let i = 0; i < tokens1.length; i++) {
    let found = false;
    for (let j = 0; j < tokens2.length; j++) {
      if (tokens1[i] === tokens2[j]) {
        found = true;
        break;
      }
    }
    if (!found) {
      result += tokens1[i] + ' ';
    }
  }
  return result.trim();
}
function uniqueTokens(str1, str2) {
  const tokens1 = str1.split(' ');
  const tokens2 = str2.split(' ');
  let unique = [];

  for (let i = 0; i < tokens1.length; i++) {
    for (let j = 0; j < tokens2.length; j++) {
      if (tokens1[i] === tokens2[j]) {
        continue; // Skip matching tokens
      }
    }
    unique.push(tokens1[i]);
  }

  return unique.join(' ');
}


  let lowerCaseString = string.toLowerCase();
  let distinctCharacters = new Set(lowerCaseString);
  let count = 0;

  for (let char of distinctCharacters) {
    if (char >= 'a' && char <= 'z') {
      count++;
    }
  }

  return count;
}
console.log(countDistinctCharacters('xyzXYZ')); // 3
console.log(countDistinctCharacters('Jerry')); // 4


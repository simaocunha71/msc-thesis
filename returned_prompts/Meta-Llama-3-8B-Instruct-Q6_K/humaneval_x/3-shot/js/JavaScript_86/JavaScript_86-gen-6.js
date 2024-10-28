  let result = '';
  let words = s.split(' ');

  for (let word of words) {
    let sortedWord = '';
    for (let char of word) {
      sortedWord += char.toLowerCase().split('').sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('');
    }
    result += sortedWord + ' ';
  }

  return result.trim();
}
// Trim is used to remove the extra space at the end of the result string.
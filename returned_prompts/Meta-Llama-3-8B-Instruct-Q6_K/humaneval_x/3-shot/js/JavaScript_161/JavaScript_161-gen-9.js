  let result = '';
  for (let char of s) {
    if (char.match(/[a-zA-Z]/)) {
      result += char === char.toLowerCase() ? char.toUpperCase() : char.toLowerCase();
    } else {
      result += char;
    }
  }
  return result.split('').reverse().join('');
}
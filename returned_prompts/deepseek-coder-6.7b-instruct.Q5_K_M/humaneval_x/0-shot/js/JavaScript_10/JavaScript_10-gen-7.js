  const count = new Array(256).fill(0);
  for (let i = 0; i < string.length; i++) {
    count[string.charCodeAt(i)]++;
  }

  let odd = 0;
  let oddChar = '';
  for (let i = 0; i < 256; i++) {
    if ((count[i] & 1) === 1) {
      odd++;
      oddChar = String.fromCharCode(i);
    }
  }

  if (odd > 1) {
    return '';
  }

  let start = new Array(256).fill(0);
  let end = new Array(256).fill(0);
  let mid = '';
  let palindrome = '';
  for (let i = 0; i < string.length; i++) {
    let char = string.charCodeAt(i);
    if ((count[char] & 1) === 1) {
      mid = String.fromChar
  let result = '';
  for (let i = 0; i <= n; i++) {
    result += i + ' ';
  }
  return result.trim();
}
// or
const stringSequence = (n) => {
  return Array(n + 1).join(' ').split(' ').filter(Boolean).join(' ');
}
// or
const stringSequence = (n) => {
  return [...Array(n + 1)].map(String).join(' ');
}
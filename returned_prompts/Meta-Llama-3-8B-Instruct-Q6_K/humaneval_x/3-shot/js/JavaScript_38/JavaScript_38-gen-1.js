  let result = '';
  for (let i = 0; i < s.length; i += 3) {
    if (i + 3 <= s.length)
      result += s[i] + s.slice(i + 1, i + 3).split('').reverse().join('');
    else
      result += s.slice(i);
  }
  return result;
}
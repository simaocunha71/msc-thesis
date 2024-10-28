  var result = '';
  for (let i = 0; i < s.length; i += 3) {
    result += s.slice(i, i + 3)[2] + s.slice(i, i + 3)[0] + s.slice(i, i + 3)[1];
  }
  return result;
}
  var result = '', temp = '';
  for (let i = 0; i < s.length; i++) {
    temp += s[i];
    if (temp.length == 3) {
      result += temp[2] + temp[0] + temp[1];
      temp = '';
    }
  }
  return result;
}
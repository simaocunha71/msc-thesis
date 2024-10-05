  var result = [];
  var is_palindrome = true;

  for (const s_char of s) {
    var is_delete = false;
    for (const c_char of c) {
      if (s_char == c_char) {
        is_delete = true;
        break;
      }
    }
    if (!is_delete) {
      result.push(s_char);
    }
  }

  for (let i = 0; i < result.length / 2; i++) {
    if (result[i] != result[result.length - i - 1]) {
      is_palindrome = false;
      break;
    }
  }

  return [result.join(''), is_palindrome];
}




  let result = [];
  let is_palindrome = true;

  for (let i = 0; i < s.length; i++) {
    if (!c.includes(s[i])) {
      result.push(s[i])
    } else {
      is_palindrome = false;
    }
  }

  return [result.join(''), is_palindrome];
}




  let result = [];
  let a_str = a.toString();
  let b_str = b.toString();
  let min_length = Math.min(a_str.length, b_str.length);

  for (let i = 0; i < min_length; i++) {
    if (parseInt(a_str[i]) % 2 == 0) {
      result.push(a_str[i]);
    }
    if (parseInt(b_str[i]) % 2 == 0) {
      result.push(b_str[i]);
    }
  }

  if (a_str.length > b_str.length) {
    result.push(b_str);
  } else if (a_str.length < b_str.length) {
    result.push(a_str);
  }

  return result.sort();
}



